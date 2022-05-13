# picoCTF 2018

<h5> leak me </h5>
<hr>

<h5> Solution </h5>

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int flag() {
  char flag[48];
  FILE *file;
  file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(flag, sizeof(flag), file);
  printf("%s", flag);
  return 0;
}


int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  
  // real pw: 
  FILE *file;
  char password[64];
  char name[256];
  char password_input[64];
  
  memset(password, 0, sizeof(password));
  memset(name, 0, sizeof(name));
  memset(password_input, 0, sizeof(password_input));
  
  printf("What is your name?\n");
  
  fgets(name, sizeof(name), stdin);
  char *end = strchr(name, '\n');
  if (end != NULL) {
    *end = '\x00';
  }

  strcat(name, ",\nPlease Enter the Password.");

  file = fopen("password.txt", "r");
  if (file == NULL) {
    printf("Password File is Missing. Problem is Misconfigured, please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(password, sizeof(password), file);

  printf("Hello ");
  puts(name);

  fgets(password_input, sizeof(password_input), stdin);
  password_input[sizeof(password_input)] = '\x00';
  
  if (!strcmp(password_input, password)) {
    flag();
  }
  else {
    printf("Incorrect Password!\n");
  }
  return 0;
}
```

<p> 바이너리를 실행하면 name 변수에 입력을 받게 됩니다. </p>
<p> 변수의 크기는 256Byte 로 지정되어 있고 지정 크기 이상으로 값을 주게 되면 </p>
<p> 메모리 오버플로우에 의해서 의도하지 않게 password.txt 의 내용을 출력해주게 됩니다. </p>

<img class="border-shadow" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FcUkVxM%2FbtqxS5oMNi8%2FfgBIokYlkgpxEHYLiakTBk%2Fimg.png"><br>

<p> 260Byte 의 메모리 오버플로우를 발생 시킨 결과로, 출력문의 끝에 패스워드가 포함된 것을 확인할 수 있습니다. </p>

<p> 해당 패스워드를 가지고, name & password 에 값을 입력시켜주면 플래그를 획득할 수 있습니다. </p>

```py
#!/usr/bin/python

from pwn import *

p = remote('2018shell.picoctf.com',31045)

name = "jhyeon"

p.sendline(name)

password = "a_reAllY_s3cuRe_p4s$word_d98e8d"

p.sendline(password)

p.interactive()
``` 
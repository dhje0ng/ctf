#!/usr/bin/python

from pwn import *

p = remote('2018shell.picoctf.com',31045)

name = "jhyeon"

p.sendline(name)

password = "a_reAllY_s3cuRe_p4s$word_d98e8d"

p.sendline(password)

p.interactive()
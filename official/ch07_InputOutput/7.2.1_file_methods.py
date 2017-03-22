
import os
from os.path import dirname

file_path = dirname(os.path.abspath(__file__)) + '/workfile'

f = open(file_path, 'r+')

#print(f.read())
#print(f.read())

#print(f.readline())
#print(f.readline())
for line in f:
    print(line, end='')
print(f.write('This is a test\n'))
f.close()


f = open(file_path, 'rb+')
print(f.write(b'0123456789abcdef'))
print(f.seek(5))
print(f.read(1))
print(f.seek(-3, 2))
print(f.read(1))
f.close()
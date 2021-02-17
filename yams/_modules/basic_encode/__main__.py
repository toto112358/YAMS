from .main import *
import sys
'''
usage: yams basic_encode [encode/decode]
'''

imput = ""
with sys.stdin as f:
    for line in f.readlines():
        imput += line


if sys.argv[1] == 'decode':
    to_decode = ''
    for num in imput:
        if '0' <= num <= '9':
            to_decode += num
    print(decode(int(to_decode)))

if sys.argv[1] == 'encode':
    print(encode(imput))

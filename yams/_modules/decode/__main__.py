# -*- coding: utf-8 -*-
import sys


decode_module = '.._basic_encode_decode'
decode_func = 'decode'
exec(f'from {decode_module} import {decode_func} as decode')

imput = ""
with sys.stdin as f:
    for line in f.readlines():
        imput += line

to_decode = ''
for num in imput:
    if '0' <= num <= '9':
        to_decode += num
print(decode(int(to_decode)), end='')

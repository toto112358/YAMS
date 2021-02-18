import sys


encode_module = '.._basic_encode_decode'
encode_func = 'encode'
exec(f'from {encode_module} import {encode_func} as encode')

imput = ""
with sys.stdin as f:
    for line in f.readlines():
        imput += line

print(encode(imput), end='')

# -*- coding: utf-8 -*-
import sys
from ...._modules._algos.twofish import *
secret_key = b'by luca and serge'
print_raw = False

imput = ""
with sys.stdin as f:
    for line in f.readlines():
        imput += line

T = Twofish(secret_key)

encrypted = encrypt(bytes(imput, 'utf-8'), secret_key)

if print_raw == "Yes, I know what I'm doing":
    exec(f'raw_bytes = """{encrypted[2:-1]}"""')
    print(raw_bytes, end='')
else:
    p(encrypted)

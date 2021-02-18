import sys
from ...._modules._algos.twofish import *
secret_key = b'by luca and serge'

imput = ""
with sys.stdin as f:
    for line in f.readlines():
        imput += line

T = Twofish(secret_key)

encrypted = encrypt(bytes(imput, 'utf-8'), secret_key)

p(encrypted)

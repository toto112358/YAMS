import sys
from ...._modules._algos.twofish import *
secret_key = b'by luca and serge'

imput = ""
with sys.stdin as f:
    for line in f.readlines():
        imput += line

T = Twofish(secret_key)

exec(f'decrypted = decrypt(b"""{imput}""", secret_key)')

print(decrypted.strip(b'\x00').decode(), end='')

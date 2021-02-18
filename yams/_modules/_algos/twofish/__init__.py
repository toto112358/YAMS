from twofish import Twofish
# 16 bytes blocks
from ...._modules._patched_classes.bytes import *
# better __str__ and __repr__ for byte
p = bytes.pretty_print

def encrypt(msg: bytes, key: bytes):
    T = Twofish(key)
    output = bytes('', 'utf-8')
    while len(msg) % 16:
        msg += bytes(chr(0), 'utf-8')

    while msg:
        output += T.encrypt(msg[:16])
        msg = msg[16:]

    return(output)

def decrypt(msg: bytes, key: bytes):
    T = Twofish(key)
    output = bytes('', 'utf-8')
    while msg:
        output += T.decrypt(msg[:16])
        msg = msg[16:]

    return(output)

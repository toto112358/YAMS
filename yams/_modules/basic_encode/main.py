from baseXtoY import baseXtoY
'''
gets input, returns coded output
'''


def encode(word):
    codes = [ord(c) for c in word]
    return str(sum(codes[i] * 256 ** i for i in range(len(codes))))

def decode(num):
    decoded = ''
    while num:
        decoded += chr(num % 256)
        num = num // 256
    return decoded

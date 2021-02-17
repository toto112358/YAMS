'''
gets input, returns coded output
'''

def encode(word):
    codes = [ord(c) for c in word]
    return str(sum(codes[i] * 256 ** i for i in range(len(codes))))


def decode(num):
    if num:
        return chr(num % 256) + decode(num // 256)
    else:
        return ""

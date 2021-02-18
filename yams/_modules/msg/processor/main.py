# -*- coding: utf-8 -*-
encode_module = '...._modules._basic_encode_decode'
encode_func = 'encode'
exec(f'from {encode_module} import {encode_func} as encode')

def process(msg):
    msg = msg.split(' ')
    author = msg[0]
    body = ''.join(msg[1:])
    return f'{author} {encode(body)}'

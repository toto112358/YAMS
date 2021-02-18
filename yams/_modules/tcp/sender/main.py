# -*- coding: utf-8 -*-
import socket
import sys


'''
Reads message from the standart input, and sends it
arguments:
    HOST:PORT

Don't forget to include the charset at last line of msg
'''


def send_message(message, destination: tuple):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(destination)
        sock.sendall(bytes(message + '\n', 'utf-8'))

        received = str(sock.recv(1024), 'utf-8')

    print(f'Sent: {message}')
    print(f'Received: {received}')

if 'yams._modules' in __name__:
    args = sys.argv
    host, port = args[1].split(':')
    port = int(port)
    message = sys.stdin.read()[:-1]
    send_message(message, (host, port))

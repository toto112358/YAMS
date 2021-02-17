import socket
import sys
'''
Reads message from the standart input,
main.py username host:port

if message == 'get_msg()': server will send all message pending
non encrypted messages are treated as commands by the server.
'''


args = sys.argv[1:]
username = args[0]
HOST, PORT = args[1].split(':')
PORT = int(PORT)


def send_message(username, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(username+ ' ' + message + '\n', 'utf-8'))

        received = str(sock.recv(1024), 'utf-8')

    print(f'Sent: {message}')
    print(f'Received: {received}')

message = sys.stdin.read()[:-1]
send_message(username, message)

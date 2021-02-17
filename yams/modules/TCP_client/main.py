import socket
import sys
'''
Reads message from the standart input, and sends it
arguments:
    HOST:PORT

Don't forget to include the charset at last line of msg
'''


def send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(message))

        received = str(sock.recv(1024), 'utf-8')

    print(f'Sent: {message}')
    print(f'Received: {received}')

if __name__ == '__main__':
    destination = tuple(args[1].split(':'))  # HOST:PORT
    PORT = int(PORT)
    message = sys.stdin.read()[:-1]
    send_message(message, destination)

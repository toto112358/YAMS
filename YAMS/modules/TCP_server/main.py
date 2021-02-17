import sys
import socketserver


args = sys.argv[1:]
HOST, PORT = args[0].split(':')
PORT = int(PORT)


class TCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline()
        self.client_name = str(self.data).split(' ')[0]
        self.message = ' '.join(str(self.data).split(' ')[1:])
        print(f'{self.client_name} wrote {self.message}')
        self.request.sendall(bytes(self.message))

with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
    server.serve_forever()

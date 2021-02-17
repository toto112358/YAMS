import sys
import socketserver


class StreamTCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline().strip()


class TCPHandler(StreamTCPHandler):
    def handle(self):
        super().handle()
        self.client_name = str(self.data).split(' ')[0]
        self.message = ' '.join(str(self.data).split(' ')[1:])
        print(f'{self.client_name} wrote {self.message}')
        self.request.sendall(bytes(self.message))


if __name__ == '__main__':
    args = sys.argv[1:]
    HOST, PORT = args[0].split(':')
    PORT = int(PORT)

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()

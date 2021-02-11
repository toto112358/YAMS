import socketserver


class TCPHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline()
        print(f'{self.client_address[0]} a écrit {self.data}')
        self.wfile.write(self.data.upper())

with socketserver.TCPServer(("localhost", 1111), TCPHandler) as server:
    server.serve_forever()

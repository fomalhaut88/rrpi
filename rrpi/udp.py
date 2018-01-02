import socket
import traceback


class Server:
    CHUNK_SIZE = 1024

    def __init__(self, host, port, handler):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind((host, port))
        self._handler = handler

    def __del__(self):
        self._sock.close()

    def listen(self):
        while True:
            try:
                in_data, address = self._sock.recvfrom(self.CHUNK_SIZE)
                out_data = self._handler(in_data)
                self._sock.sendto(in_data, address)

            except Exception:
                traceback.print_exc()


class Client:
    CHUNK_SIZE = 1024

    def __init__(self, host, port):
        self._host = host
        self._port = port

    def send(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data, (self._host, self._port))
        return output

import socket
from threading import Thread
import json
from utils import *


def client_handshake(clientsocket, clientaddress):
    data = receive_json(clientsocket)
    print(data)
    send_json(clientsocket, {"message": "Greetings"})


class Server:
    def __init__(self, port=62626):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(("", port))
        self.server.listen()

    def main_listen_loop(self):
        """
        Listen for incoming client.
        It's the main gate to our protocol, then it dispatches the client into different lobby.
        :return:
        """
        error = False
        while not error:
            print("Waiting for a client")
            clientsocket, clientaddress = self.server.accept()
            Thread(target=client_handshake, args=(clientsocket, clientaddress)).start()


if __name__ == "__main__":
    serv = Server(62626)
    serv.main_listen_loop()
import pytest
import socket
import json


def test_main_listen_loop():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 62626))
    sock.sendall(json.dumps({"hllo": "bro"}).encode('utf-8'))
    data = sock.recv(1024)
    assert data == b'{"message": "Greetings"}'
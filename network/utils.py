import socket
import json

def receive_json(clientsocket):
    try:
        data = clientsocket.recv(1024).decode("utf-8")
        return json.loads(data)
    except json.JSONDecodeError:
        print("Invalid JSON")
    except OSError:
        raise OSError("Connection with server is broken")

def send_json(clientsocket, data_dict):
    try:
        clientsocket.send(json.dumps(data_dict).encode("utf-8"))
    except OSError:
        raise OSError("Erreur dans l'envoie d'un message")
    except json.JSONDecodeError:
        print("Invalid dictionary")

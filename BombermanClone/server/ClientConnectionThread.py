import socket
from threading import Thread
import pickle


class ClientConnectionThread(Thread):
    def __init__(self, client_socket, client_address, messageHandeler):
        super().__init__()
        self.is_alive = True
        self.client_socket = client_socket
        self.client_address = client_address
        self.messageHandlingFunction = messageHandeler

    def run(self):
        while self.is_alive:
            try:
                self.recieveData()

            except socket.error as e:
                print(f"ClientConnectionThread recieve error: {e}")
                self.is_alive = False


    def recieveData(self):
        data = self.client_socket.recv(1024)

        message = pickle.loads(data)
        self.messageHandlingFunction(self, message)

    def sendData(self, data):
        if not self.is_alive:
            return

        try:
            message = pickle.dumps(data)
            self.client_socket.sendall(message)
        except Exception as e:
            print(f"ClientConnectionThread sendData Error: {e}")
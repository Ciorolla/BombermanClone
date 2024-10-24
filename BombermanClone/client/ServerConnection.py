import socket
import pickle
from threading import Thread

class ServerConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.message_listener = None

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

        self.receive_thread = Thread(target=self.receive_messages)
        self.receive_thread.start()

    def close(self):
        self.client_socket.close()
        self.receive_thread.join()

    def listenForMessages(self, listener):
        self.message_listener = listener

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    print(f"Client disconnected")
                    break

                message = pickle.loads(data)
                if self.message_listener:
                    self.message_listener(message)
                else:
                    print(f"Received unhandled message: {message}")


            except socket.error as e:
                print(f"Error during data retrieval: {e}")
                return

            except pickle.UnpicklingError as e:
                print(f"Error unpickling message: {e}")


    def send_message(self, message):
        try:
            self.client_socket.sendall(pickle.dumps(message))
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    client = ServerConnection("localhost", 8888)
    client.connect()

    try:
        while True:
            message = input("Enter message: ")
            client.send_message(message)

    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Closing connection.")
        client.close()
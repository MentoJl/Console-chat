import socket
from threading import *


class Server:
    HOST = "127.0.0.1"
    PORT = 100
    clients = {}
    server = socket.socket()

    def client_connect(self, connect, address):
        client_name = connect.recv(1024).decode()
        self.clients[address] = connect
        print(f"{client_name} connected")
        while True:
            try:
                data = connect.recv(1024)
                if data:
                    message = f"{client_name}: {data.decode()}"
                    print(message)
                    self.send_clients(message, connect)
                else:
                    self.remove_client(client_name, address)
                    break
            except:
                self.remove_client(connect, client_name, address)
                break

    def send_clients(self, message, connect):
        for client in self.clients.values():
            if client != connect:
                client.sendall(message.encode())

    def remove_client(self, connect, name, address):
        print(f"{name} disconnected")
        del self.clients[address]
        self.send_clients(f"{name} disconnected", connect)

    def run_server(self):
        self.server.bind((self.HOST, self.PORT))
        self.server.listen()
        print(f"Server success running on {self.HOST}:{self.PORT}")
        while True:
            connect, address = self.server.accept()
            print(f"{address} is running now")
            thread = Thread(target=self.client_connect, args=(connect, address))
            thread.start()

chat = Server()
chat.run_server()
import socket
from threading import *


HOST = '127.0.0.1'
PORT = 100
mess = ""

def get_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if data:
                
                print(data.decode())
        except:
            break

client = socket.socket()
client.connect((HOST, PORT))
client_name = input("Input your name: ")
client.sendall(client_name.encode())
thread = Thread(target=get_messages, args=(client,))
thread.start()
while True:
    message = input()
    client.sendall(message.encode())
import socket

socket_server = socket.socket()

name = input("Введите имя: ")
socket_server.connect(("127.0.0.1", 50))
socket_server.send(name.encode())
socket_name = socket_server.recv(1024)
server_name = socket_name.decode()
print (server_name,  "присоеденился")

while True:
    message = (socket_server.recv(1024)) .decode()
    print(server_name, ":", message)
    message = input("Me: ")
    socket_server.send(message.encode())
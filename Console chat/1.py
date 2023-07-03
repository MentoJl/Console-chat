import socket

new_socket = socket.socket ()
new_socket.bind(("127.0.0.1", 50))
new_socket.listen()

print("Сервер запущен!")
name = input("Name:")
conn, add = new_socket.accept()

client = (conn.recv(1024)).decode()
print(client + " Connect")
conn.send(name.encode())

while True:
    client = (conn.recv(1024)).decode()
    print(client + " Connect")
    conn.send(name.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
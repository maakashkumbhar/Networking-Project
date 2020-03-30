"""
import socket

server = "192.168.1.207"
port = 5555
#SocketServer object
socketsever= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##Binding the SocketServer To the Port
try:
    socketsever.bind((server,port))
except socket.error as e:
    str(e)
##Listening To the  Connection
socketsever.listen(2)
print("Server Started, Waiting for Connection")
while True:
    conn,addr = socketsever.accept()
    print("Client One Connected:")
    conn.send("Welcome to the Server:".encode())
    conn1,addr = socketsever.accept()
    print("Client two Connected:")
    conn1.send("Welcome to the Server:".encode())
    from_client1 = conn.recv(1024)
    print(from_client1)
    from_client2 = conn1.recv(1024)
    print(from_client2)

"""
import socket
from _thread import *

server = "192.168.1.207"
port  = 1234

socketsever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    socketsever.bind((server,port))
except socket.error as e:
    print(str(e))

socketsever.listen()
print("Waiting For Connection>>>>>")
def client_thread(conn):
    reply = "Welcome To The Jungle"
    conn.send(reply.encode())
    while True:
        message_from_client = conn.recv(2048)
        print(message_from_client.decode('utf-8'))
        conn.sendall(bytes(message_from_client))
        if not message_from_client:
            break
    conn.close()
while True:
    conn,addr = socketsever.accept()
    print("Connected To>>>",addr)
    start_new_thread(client_thread,(conn,))
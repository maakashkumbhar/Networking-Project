import socket

server = "192.168.1.207"
port  = 1234

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect((server,port))
while True:
    msg = clientsocket.recv(2048)
    print(msg.decode("utf-8"))
    while True:
        message_to_send = str(input("Client2:"))
        actual_msg = "Client1:" + message_to_send
        message = actual_msg.encode()
        clientsocket.send(message)
        exit = 0
        if message_to_send==str(exit):
            break
clientsocket.close()
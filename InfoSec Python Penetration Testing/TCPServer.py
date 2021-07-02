#!/usr/bin/python3
import socket

# Creating the socket object
server_scocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# host = 'ip in string'
host = socket.gethostname()
port = 3000

# Binding to socket
server_scocket.bind((host,port))

# Starting TCP server
server_scocket.listen(3)

while True:
    # Starting the connection
    client_socket, address = server_scocket.accept()
    
    print("recieved connection from %s " % str(address))

    message = 'Yo! Thank you for connecting to this server!' + '\r\n'
    client_socket.send(message.encode('ascii'))

    client_socket.close()
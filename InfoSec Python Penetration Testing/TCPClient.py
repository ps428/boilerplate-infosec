#!/usr/bin/python3

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '192.168.1.104'
host = socket.gethostname()

port = 3000

client_socket.connect((host, port))

message = client_socket.recv(1024) 

client_socket.close()

print(message.decode('ascii'))
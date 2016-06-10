import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 134                # Reserve a port for your service.

s.connect((host, port))

while 1:
    message = input()
    s.send(bytes(message,'utf-8'))
    print(s.recv(1024))

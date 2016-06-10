import socket


serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

port = 134
serversocket.bind((socket.gethostname(), port)) 

serversocket.listen(1)

while 1:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()
    print(address)
    #now do something with the clientsocket
    message = input()
    clientsocket.send(bytes(message,'utf-8'))
    print(clientsocket.recv(1024))

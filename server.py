import socket

#create an INET, STREAMing socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
port = 134
serversocket.bind((socket.gethostname(), port)) 
#become a server socket
serversocket.listen(1)

while 1:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()
    print(address)
    #now do something with the clientsocket
    #in this case, we'll pretend this is a threaded server
    message = input()
    clientsocket.send(bytes(message,'utf-8'))
    print(clientsocket.recv(1024))

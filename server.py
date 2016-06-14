import socket
from servercommands import commands

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

port = input("Enter port \n")
portenter = int(port)
serversocket.bind((socket.gethostname(), portenter)) 

serversocket.listen(90)

 
while 1:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()
    print("Connected: ")
    print(address)
    #now do something with the clientsocket
    message = input("Enter command: \n")
    if(commands.checkcommand(message) == False):
        print("Not a valid command \n")
        continue
    
    else:
      if(commands.checkcommand(message) == "visitsite"):
          url = input("Enter URL")
          message = url
          
          
        
          
            
      clientsocket.send(bytes(message,'utf-8'))
      continue
    
    
    

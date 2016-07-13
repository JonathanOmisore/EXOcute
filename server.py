import socket
import servercommands

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

port = input("Enter port \n")
portenter = int(port)
host = input("Enter server host address \n")
serversocket.bind((host, portenter)) 

serversocket.listen(90)
def getinput():
    message = input("Enter command: \n")
    return message
def start():
    
    (clientsocket, address) = serversocket.accept()
    print("Connected: ")
    print(address)
    while 1:
        
    #accept connections from outside
        
    #now do something with the clientsocket
        thecommand = getinput()
        if(servercommands.checkdictionary(thecommand) == False):
            
            print("Command not in dictionary \n")
            
            
        else:

            
            if(servercommands.checkdictionary(thecommand) == "visitsite"):
                
                url = input("Enter URL \n")
                thecommand = url
          
          
        
          
            
            clientsocket.send(bytes(thecommand,'utf-8'))
            
start()

import socket
from servercommands import checkdictionary

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

port = input("Enter port \n")
portenter = int(port)
serversocket.bind((socket.gethostname(), portenter)) 

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
        if(checkdictionary(thecommand) == False):
            
            print("Not a valid command \n")
            
            
    
        else:
            
            if(checkdictionary(thecommand) == "visitsite"):
                
                url = input("Enter URL")
                thecommand = url
          
          
        
          
            
            clientsocket.send(bytes(thecommand,'utf-8'))
            
start()

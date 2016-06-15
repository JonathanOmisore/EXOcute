import socket               # Import socket module
import webbrowser
import sys
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 134                # Reserve a port for your service.

s.connect((host, port))

while True:
    
    
    received = s.recv(1024).decode(encoding="utf-8")
    if(received == "close"):
        
    
        sys.exit()
    if(received[:7] == "http://"):
        
    
        
        
        webbrowser.open(received)
        
        

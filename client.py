import socket               # Import socket module
import webbrowser
import sys
s = socket.socket()         # Create a socket object
host = "127.0.0.1" # Server that client will connect to
port = 134                # Server's port that client will use

s.connect((host, port))

while True:
    
    
    received = s.recv(1024).decode(encoding="utf-8")
    if(received == "close"):
        
    
        sys.exit()
    if(received[:7] == "http://"):
        
    
        
        
        webbrowser.open(received)
        
        

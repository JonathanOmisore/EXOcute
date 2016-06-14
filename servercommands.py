import socket
class commands:
    def checkcommand(word):
        commandlist = ['close','visitsite']
        if(word in commandlist):
            return word
        else:
            return False
        

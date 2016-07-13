def checkdictionary(command):
    
    commanddictionary = ['visitsite:','close']
    for x in range(len(commanddictionary)):
        for command in commanddictionary:
            
            if command in word:
                return word
        else:
        
            return False

    commanddictionary = ['close','visitsite']
    if(command in commanddictionary):
        
        return command
    else:
        
        return False
        

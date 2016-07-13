def checkdictionary(word):
    commanddictionary = ['visitsite:','close','shell:']
    for x in range(len(commanddictionary)):
        for command in commanddictionary:
            
            if command in word:
                return word
        else:
        
            return False

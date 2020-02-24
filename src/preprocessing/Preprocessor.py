import dateutil.parser

class Preprocessor:
    def __init__(self,inputList):
        self.dic = {}
        self.list = inputList
        
    
    def parseDateTime(self):
        for item_index in range(len(self.list)):
            temp = str(dateutil.parser.parse(self.list[item_index][4]))
            self.list[item_index].append(temp)
            
        return self.list
    
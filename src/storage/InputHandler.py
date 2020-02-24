import csv

class InputHandler:
    def __init__(self, inputFileName):
        self.inputFile = inputFileName
        self.store = []
        
    
    def parse(self):
        #Read file
        with open(self.inputFile, 'r') as f:
            reader = csv.reader(f)
            
            next(reader)
            for row in reader:
                self.store.append(row)
                
        
        return self.store
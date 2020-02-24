import pandas as pd

class OutputHandler:
    def __init__(self, outputDir):
        self.outputDir = outputDir
        
    def save_to_csv(self,header,output):
        save = []
        
        #Add header data in list
        save.append(header)
        
        #Merge both header and output
        save = save + output

        #Pandas to parse the list
        df =  pd.DataFrame(save)
        
        #save to csv
        df.to_csv(self.outputDir+'/report.csv', sep=',', header=None, index=False)
        
        return "Saved! Successfully"
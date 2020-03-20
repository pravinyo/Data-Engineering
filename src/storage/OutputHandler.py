import csv

class OutputHandler:
    def __init__(self, outputFilePath):
        self.outputFilePath = outputFilePath
        
    def save_to_csv(self,header,output):


        with open(self.outputFilePath, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(output)
'''
        save = []
        
        #Add header data in list
        save.append(header)
        
        #Merge both header and output
        save = save + output

        #Pandas to parse the list
        df =  pd.DataFrame(save)
        
        #save to csv
        print("Path:"+self.outputFilePath)
        df.to_csv(self.outputFilePath, sep=',', header=None, index=False)
        
        return "Saved! Successfully"
'''
        #save to csv
        print("Path:"+self.outputFilePath)
        return "Saved! Successfully"

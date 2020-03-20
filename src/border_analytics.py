from storage.InputHandler import InputHandler
from storage.OutputHandler import OutputHandler
from preprocessing.Preprocessor import Preprocessor
from computation.BorderCrossingComputation import BorderCrossingComputation
import argparse
import sys


class BorderAnalytics:
    def __init__(self,inputFile,outputFilePath):
        self.input = inputFile
        self.outputFilePath = outputFilePath
        self.inputHandler = None
        self.outputHandler = None
        self.preprocessor = None
        self.borderCrossingCompute = None
        
    def inputFile(self,name):
        self.inputHandler = InputHandler(name)
        return self.inputHandler.parse()
        
    def preprocess(self,inputList):
        self.preprocessor = Preprocessor(inputList)
        return self.preprocessor.parseDateTime()
        
    def computeTotalCrossing(self):
        store = self.inputFile(self.input)
        print("Store size:"+str(len(store)))
        
        processedList = self.preprocess(store)
        print("List processed:"+str(len(store)))
        
        self.borderCrossingCompute = BorderCrossingComputation(processedList)
        
        print("Starting computation for total crossing")
        self.borderCrossingCompute.computeTotalCross()
        print("Finished")
        
        return self.borderCrossingCompute.get_total_cross()
    
    def computeAverageCrossing(self):
        print("Starting avg cross computation")
        self.borderCrossingCompute.calculate_running_avg()
        print("Finished")
        
        return self.borderCrossingCompute.get_monthly_avg()
    
    def startAnalysis(self):
        totalCrossing = self.computeTotalCrossing()
        avgCrossing= self.computeAverageCrossing()
        
        print("Merging results")
        output = self.borderCrossingCompute.getTotalCrossAndAverage()
        print("Finished")
        
        print("Saving output")
        self.saveOutput(output)
        
        
    def saveOutput(self,output):
        self.outputHandler = OutputHandler(self.outputFilePath)
        header = ["Border","Date","Measure","Value","Average"]
        status = self.outputHandler.save_to_csv(header,output)
        print(status)
        


try:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", help="Input csv file for Analytics")
    parser.add_argument("outputFilePath", help="dir for analytics output")
    
    args = parser.parse_args()
    
    analytics = BorderAnalytics(args.inputFile,args.outputFilePath)
    analytics.startAnalysis()
    
    
except:
    e = sys.exc_info()[0]
    print(e)
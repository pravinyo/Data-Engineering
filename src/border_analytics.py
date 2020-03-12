from computation.BorderCrossingComputation import BorderCrossingComputation
from preprocessing.Preprocessor import Preprocessor
from storage.InputHandler import InputHandler
from storage.OutputHandler import OutputHandler


class BorderAnalytics:
    def __init__(self,inputFile,outputDir):
        self.input = inputFile
        self.outputDir = outputDir
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
        self.saveOutput(self.outputDir,output)
        
        
    def saveOutput(self,outputDir,output):
        self.outputHandler = OutputHandler(self.outputDir)
        header = ["Border","Date","Measure","Value","Average"]
        status = self.outputHandler.save_to_csv(header,output)
        print(status)
        

        
# Here we start the analysis
inputFile = "../input/Border_Crossing_Entry_Data.csv"
#testInput = "../insight_testsuite/tests/test_1/input/Border_Crossing_Entry_Data.csv"
#testOutput = "../insight_testsuite/tests/test_1/output/report.csv"
outputDir = "../output/"

analytics = BorderAnalytics(inputFile,outputDir)
#analytics = BorderAnalytics(testInput,testOutput)
analytics.startAnalysis()
import datetime

class BorderCrossingComputation:
    def __init__(self,inputList):
        self.dic = {}
        self.list = inputList
        self.totalCross = []
    
    #Utility functions
    def print_avg(ref):
        for key,value in ref.items():
            print("Average for "+key+ " is :"+str(round(value)))

    def gen_key(self,border,means):
        return border+"#"+means

    def gen_key2(self,border,date,means):
        return border+"#"+date+"#"+means
    
    #Compute total cross occured at each border for all Measure
    def computeTotalCross(self):
        #dictionary to hold the counts of entity based on Key(Border,date,Measure) and value(count)
        
        for index in range(len(self.list)):
            key = tuple(self.list[index][3:6]) #Key(Border,date,Measure)
            value = int(self.list[index][6]) #value(count)
            
            if key in self.dic:
                self.dic[key] += value
            else:
                self.dic[key] = value
                
        self.totalCross = self.transformResults()
        print(self.totalCross)
        
    
    def get_total_cross(self):
        return self.totalCross
    
    def transformResults(self):
        #data structure of each item is [Border,date,Measure,count]
        arr = []
        
        for i in self.dic.keys():
            temp = list(i)
            temp.append(self.dic[i])
            arr.append(temp)
            
        return self.sortResults(arr)
    
    def sortResults(self,listArray):
        #returned list will be sorted in following order(date -> value -> Measure -> border)
        newArray = sorted(listArray, key=lambda x: (x[1], x[3], x[2], x[0]))
        newArray.reverse()
        return newArray
    
    
    #Time complexity is O(n)+O(time_required_to_sort) , assuming saving and retrival cost of dic is constant
    def calculate_running_avg(self,border_index=0,date_index=1,means_index=2,value_index=3):
        #running average
        run_avg = {}
        return_avg = {}

        #For simplicity lets sort the dic in ascending order of date
        td = sorted(self.get_total_cross(), key=lambda x: datetime.datetime.strptime(x[date_index], '%m/%d/%y %H:%M'))
        #print(td)

        #traverse list once and calculate avg and save in dic
        for item in td:
            key = self.gen_key(item[border_index],item[means_index])
            key2 = self.gen_key2(item[border_index],item[date_index],item[means_index])

            if(key in run_avg):
                value = run_avg[key]
                print("Log: Before:"+str(value))
                return_avg[key2] = value[0]/value[1]

                value[0]+=int(item[value_index])
                value[1]+=1
                run_avg[key] = value
                print("Log: After: adding "+str(item[value_index])+"is "+str(run_avg[key]))

            else:
                return_avg[key2] = 0
                value = [int(item[value_index]),1] #total,count
                run_avg[key] = value
        
        self.avg_monthly_run = return_avg
    
    def get_monthly_avg(self):
        return self.avg_monthly_run
    
    def getTotalCrossAndAverage(self):
        output = []

        for i in self.totalCross:
            temp = list(i)
        
            key = self.gen_key2(temp[0],temp[1],temp[2])
            temp.append(int(round(self.avg_monthly_run[key])))
            
            output.append(temp)
            
        return output
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import json
import sys

class DataOperations:
    _dataFrameObj = pd.DataFrame(data=([]))
    DATA_COUNT = 100
    
    #setting mod for every type of data to visualize
    mod = 0
    
    '''
    if class don't have any parameter, we creating own dataset. 
    x1 and x2 are values for creating dataset.
    '''
    
    x1 = ()
    x2 = ()
    
    def __init__(self, *args):
        
        if len(args) < 1: 
            
            '''This part of the code is going to work when class don't have any parameter. 
            Then create own dataset and convert to pandas dataframe'''
            
            self.x1 = np.random.randint(0, 50, size=self.DATA_COUNT) 
            self.x2 = np.random.randint(0, 50, size=self.DATA_COUNT) 
            d = ( self.x1, self.x2 )
            df = pd.DataFrame(data=d)
            self._setDataFrame(df) 
            self.mod = 1
            
        else:            
            if isinstance(args[0], str):
                #with path(json or csv)
                #If class have path as parameter this part of code is going to work
               
                try:
                   #Handling for JSON
                   #Checking the path if it has json or csv file
                 
                    file = open(args[0])
                    json_file = json.loads(file.read())
                    file.close()
                    pandas_object_json = pd.read_json(args[0])
                    self._setDataFrame(pandas_object_json) 
                    self.mod = 2
                    return
                except:
                    pass
                try:
                    #Handling for CSV
                    pandas_object_csv = pd.read_csv(args[0])
                    self._setDataFrame(pandas_object_csv) 
                    self.mod = 3
                    return
                except:
                    pass
                #When giving other file type, getting error message
                print("[-] Unexpected File Type")
                sys.exit(-1)
                
            elif isinstance(args[0], np.ndarray):
                '''
                This part of the code is going to work when class have 
                numpay array as parameter
                '''
                data = pd.DataFrame(args[0])
                self._setDataFrame(data) 
                self.mod = 4
            elif isinstance(args[0], pd.DataFrame):
                '''
                This part of the code is going to work when  have
                pandas dataframe as parameter
                '''
                self._setDataFrame(args[0]) 
                self.mod = 5
 
    def statistical_values(self):
        #Calculating mean, std and IQR values
        return print(self._dataFrameObj.describe())
    
    def visualize(self):
        #Visualizing the dataset according to their mod
        
        if self.mod ==1:
           plt.scatter(self.x1, self.x2)
           plt.show()
            
        elif self.mod == 2:
            sns.stripplot(x="species", y="sepalLength",data=self.getDataFrame())
            plt.show()
            
        elif self.mod == 3:
            sns.stripplot(x="Species", y="PetalWidthCm",data=self.getDataFrame())
            plt.show()
           
        elif self.mod == 4:
           sns.heatmap(self.getDataFrame(), annot=True, fmt="d")
           plt.show()
           
        else:
           sns.stripplot(x="species", y="petal_length",data=self.getDataFrame())
           plt.show()
            
    def _setDataFrame(self,data):
        self._dataFrameObj = data
    
    def getDataFrame(self):
        return self._dataFrameObj
            

# 1. Numpay array parameter
numpy_array = np.random.randint(10, size=(10,8))
nparray = DataOperations(numpy_array)
nparray.statistical_values()
nparray.visualize()


# 2. Get dataset from Seaborn, DataFrame parameter
'''
In homework it was saying:
    
'If pandas dataframe is given directly, it will save without any changes.'

First, I create list then conver to dataframe but the I change my mind because
I used that for numpay array. Then I made it with seaborn by hand.
 I hope I did it right
'''
sns_dataset = sns.load_dataset("iris")
df = DataOperations(sns_dataset)
df.statistical_values()
df.visualize()


# 3. Path (JSON) parameter
path_json = DataOperations("./iris.json")
path_json.statistical_values()
path_json.visualize()

# 4. Path (CSV) parameter
path_csv = DataOperations("./Iris.csv")
path_csv.statistical_values()
path_csv.visualize()

# 5. Empty(without parameter)
empty = DataOperations()
empty.statistical_values()
empty.visualize()

 
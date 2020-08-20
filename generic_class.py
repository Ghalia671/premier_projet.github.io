import json
import csv
import time

class RetData :
    def __init__(self,csvFileName = 'data.csv',jsonFileName = 'data.json'):
        self.listD = []
        self.listJ = []
        self.listConc = []
        self.csvFile = csvFileName
        self.jsonFile = jsonFileName
    def store_data_csv(self):
        """ Store csv data in a list """
        try:
            i = 0
            with open(self.csvFile, newline='') as file:
                spamreader = csv.reader(file, delimiter='\t', quotechar='\n')
                for row in spamreader:
                    i = i+1
                    if(i>1):
                        self.listD.append({"date" : row[0],"depenses" : row[1]})
                print("CSV file list data is : ",self.listD)
        except Exception as e:
            print("Problem to read csv file")
            print(e)
        else:
            print("CSV Data retrieved")
        finally :
            file.close()
            
    def store_data_json(self):
        """ Store json data in a list """
        try:
            temp_dict1 = {}
            temp_dict2 = {}
            # read file
            with open(self.jsonFile, 'r') as myfile:
                data=myfile.read()

            # parse file
            obj = json.loads(data)
            temp_dict1.update(obj['date'])
            temp_dict2.update(obj['depenses'])
            
            for i in range(5):
                self.listJ.append({"date" : temp_dict1[f'{i}'],"depenses" : temp_dict2[f'{i}']})
                
            print("JSON file list is :",self.listJ)
            
        except Exception as e:
            print("Problem to read JSON file")
            print(e)
        else:
            print("JSON Data retrieved")
        finally :
            myfile.close()

    def concatenateLists(self):      
        self.listConc.append(self.listD)
        self.listConc.append(self.listJ)
        print("List concatenated is :",self.listConc)
        
    def startWorkFlow(self):      
        self.store_data_csv()
        self.store_data_json()
        self.concatenateLists()
        self.createJSONFile()
        self.createCSVFile()
        
    def createJSONFile(self):
        """ Create JSON file from a list """
        try:
            with open(f'dataConc_{time.strftime("%Y%m%d-%H%M%S")}.json', 'w') as outfile:
                json.dump(self.listConc, outfile, indent=4)
        except Exception as e:
            print("Problem to write JSON file")
            print(e)
        else:
            print("JSON Data written")
        finally :
            outfile.close()
            
    def createCSVFile(self):
        """ Create CSV file from a list """
        try:
            with open(f'dataConc_{time.strftime("%Y%m%d-%H%M%S")}.csv', 'w') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for i in range(2):
                    for j in range(5):
                        filewriter.writerow([self.listConc[i][j]['date'],self.listConc[i][j]['depenses']])
        except Exception as e:
            print("Problem to write CSV file")
            print(e)
        else:
            print("CSV Data written")
        finally :
            csvfile.close()
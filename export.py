import csv

__author__ = 'mudit'

class exportData():
    data=[]
    def __init__(self,data):
        self.data=data

    def toCSV(self,filename):
        with open(filename,'wb') as f:
            writer=csv.writer(f,delimiter=',', quotechar='"')
            writer.writerows(self.data)
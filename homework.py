import numpy as np
import plotly.express as px
import csv
def getDataSource(data_path):
    week= []
    coffee= []
    with open(data_path) as csv_files:
        csv_reader = csv.DictReader(csv_files)
        for row in csv_reader:
            week.append(float(row["week"]))
            coffee.append(float(row["Coffee"]))
        return{"x":week,"y":coffee}
def findCoRelation(data_source):
    coRelation = np.corrcoef(data_source["x"],data_source["y"])
    print("co relation is",coRelation[0,1])
def setup():
    data_path = "C:/Users/gogof/Desktop/coding/hi-main/c106/coffee.csv"
    data_source = getDataSource(data_path)
    findCoRelation(data_source)
setup()
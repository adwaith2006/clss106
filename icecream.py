import csv
import plotly.express as px
import numpy as np
with open('icecream.csv') as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x='Temperature',y='Ice-cream Sales')
    fig.show()

def getDataSource(data_path):
    temperature=[]
    icecream_sales=[]
    with open('icecream.csv') as f:
        df=csv.DictReader(f)
        for row in df:
            temperature.append(float(row['Temperature']))
            icecream_sales.append(float(row['Ice-cream Sales']))
    return {'x':temperature,'y':icecream_sales}

def findCorellation(data_source):
    corellation=np.corrcoef(data_source['x'],data_source['y'])
    print('corellation between temperature and icecream sales is:',corellation[0,1])

def setUp():
    data_path='icecream.csv'
    data_source=getDataSource(data_path)
    findCorellation(data_source)

setUp()
    
    
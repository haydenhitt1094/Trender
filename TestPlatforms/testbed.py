import datetime
import yfinance as charts
import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import math
import scipy.interpolate as spline
import stockstats

today = datetime.date.today()
startWatch = today - datetime.timedelta(days = 240)
tickerFetch = charts.Ticker(str('DIS'))
stockData = tickerFetch.history(period = '1w', start = startWatch, end = str(today))


macdData = stockstats.StockDataFrame.retype(stockData)

macdvals = []

for j in range(len(macdData)):
    #if macdData.iloc[j][1] == 0:
    
    macd = macdData['macd']
    signalline = macdData['macds']
    #print(macd[j])
    #print(signalline[j])
    print(macd[j]-signalline[j])
    print("------------")
    #macdvals.append(macdData.iloc[j][1])
#print(macdvals)       

x = []
low = []
for i in range(len(stockData)):
    low.append(stockData.iloc[i][0])
    x.append(i)



byday = dict(zip(x,low))
inves = []
inves.append(max(low))
for day in x:
   if byday[day] <= max(low) and byday[day] > float(.9)*max(low):
       plt.annotate("POI" ,xy = (day,byday[day]), arrowprops = {'facecolor':'red'})







plt.plot(x,low)
plt.show()

print("Done!!!")
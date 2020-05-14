import sqlite3 as dbase
import yfinance as charts
import datetime 
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
import scipy.interpolate as spline
import math
import time
import os 
from multiprocessing import Process,ProcessError,Array
from MemSwap import MemSwap


CurrentDirectory = os.path.dirname(os.path.abspath(__file__))
os.chdir(CurrentDirectory)

def getDistance(initialday,initialvalue,finalday,finalvalue):
    import math
    distance = math.sqrt(((finalvalue-initialvalue)**2)+((finalday-initialday)**2))
    return distance

def poolBuild(database,PoolResult):
    pool = []
    init = dbase.connect(str(database))
    cursor = init.cursor()
    for row in cursor.execute("SELECT * FROM ActivePool"):
        try:
            if row[1] == int(1):
                pool.append(str(row[0]))
                for PoolIndexer,PoolElement in enumerate(pool):
                    PoolResult[PoolIndexer] = str(PoolElement) 
            else:
                pass
        except IndexError:
            break
           

#----Elliot-Wave-Daemon---------------
def findElliot(actives):
    global ElliotConfidence 
    ElliotConfidence = 0 
    for stock in actives:
        try:
            today = datetime.date.today()
            startWatch = today - datetime.timedelta(days = 240)
            tickerFetch = charts.Ticker(str(stock))
            stockData = tickerFetch.history(period = '1d', start = startWatch, end = str(today))
            #Initial plotting
            CurrentDay = []
            CloseValue = []
            for i in range(len(stockData)):
                CloseValue.append(stockData.iloc[i][3])
                CurrentDay.append(i)
            DataByDay = dict(zip(CurrentDay,CloseValue))
            PointsOfInterest = []
            DaysOfInterest = []
            for day in CloseValue:
                if DataByDay[CurrentDay] <= max(DataByDay) and DatabyDay[CurrentDay] > float(.9)*max(DataByDay):
                   PointsOfInterest.append(DataByDay[CurrentDay])
                   DaysOfInterest.append[CurrentDay]
                   plt.annotate("POI" ,xy = (CurrentDay,DataByDay[CurrentDay]), arrowprops = {'facecolor':'red'})
                   time.sleep(5)
                   plt.close() 
            else:
                pass
            #BeginCurveTraceSequence----------------------------
            BaseTracePointDay = int(max(CurrentDay))
            BaseTracePointValue = int(DataByDay[CurrentDay])
            
            for DayIterator in range(int(BaseTracePointDay,240)):
                if DataByDay[DayIterator] >= DataByDay[int(DayIterator + 1)]:
                    CarryOn = False
                    pass
                else:
                    LegOneLength = getDistance(BaseTracePointDay,BaseTracePointValue,DayIterator,DataByDay[DayIterator])
                    CarryOn = True
                    DayIteratorLast = DayIterator
                    break
            if CarryOn == True:
                LegTwoBaseValue = max(list(DataByDay[DayIteratorLast],DataByDay[DayIteratorLast + 1],DataByDay[DayIteratorLast + 2],DataByDay[DayIterator + 3]))
                LegTwoBaseDay = 
        except IndexError:
            print("IndexError: Fatal>>> Closing...") 
            break
    



def Main():
    CurrentTime = datetime.datetime.now()
    CurrentHour = CurrentTime.hour
    CurrentMin = CurrentTime.minute
    DataBaseSizeOf = MemSwap('MasterPool.db')
    while CurrentHour == 0 and CurrentMin <= 0 and CurrentMin >= 15:
        try:
            ProcessorNodesActive = []
            ProcessorNodePossible = os.cpu_count()
            PoolResult = Array('i',DataBaseSizeOf.GetPoolSize())
            for k in range(ProcessorNodePossible):
                poolNode = Process(target = poolBuild, args = (MasterPool,PoolResult))
                ProcessorNodesActive.append(poolNode)
            for eachProcess in ProcessorNodesActive:
                eachProcess.start()
            for eachProcess in ProcessorNodesActive:
                eachProcess.join()
            for eachProcess in ProcessorNodesActive:
                eachProcess.close()
        except ProcessError:
            print("Fatal process error>>> Killing...")
            break
    
    ActiveStocks = PoolResult[:]

    while CurrentHour == 6 and CurrentMin != 59:
        try:
            ProcessorNodesActive = []
            ProcessorNodePossible = os.cpu_count()
            for j in range(ProcessorNodePossible):
                findElliotNode = Process(target=findElliot, args= (ActiveStocks,))
                ProcessorNodesActive.append(findElliotNode)
            for eachProcess in ProcessorNodesActive:
                eachProcess.start()
            for eachProcess in ProcessorNodesActive:
                eachProcess.join()
            for eachProcess in ProcessorNodesActive:
                eachProcess.close()
        except ProcessError:
            print("Fatal process error>>> Killing...")
            break




if __name__ == "__main__":
    Main()
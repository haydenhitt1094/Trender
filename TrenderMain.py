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
from MACD import MACD,WhereCross
import json
from Settings import JSONSettings


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
           

def TrendlineTrack(actives):
    for stock in actives:
        try:
            today = datetime.date.today()
            startWatch = today - datetime.timedelta(days = 10)
            tickerFetch = charts.Ticker(str(stock))
            stockData = tickerFetch.history(period = '1d', start = startWatch, end = str(today))
            
            #"Verbose" plotting
            CurrentDay = []
            CloseValue = []
            
            for i in range(len(stockData)):
                CloseValue.append(stockData.iloc[i][3])
                CurrentDay.append(i)
            PairedData = dict(zip(CurrentDay,CloseValue))
            
            CurrentStock = MACD(stockData)
            SignalLineValues = CurrentStock.getSignalLineValues()
            MACDValues = CurrentStock.getMACDValues()

            SignalSet = WhereCross(byday = list(range(0,9)), macd_vals = MACDValues, signal_vals = SignalLineValues)
            MarkedEvents = SignalSet.do()



        except IndexError:
            print("IndexError: Fatal>>> Closing...") 
            break


def getParameters(SettingsFile): 
    with open(str(SettingsFile),'r') as SettingsProfile:
            Preferences = json.load(SettingsProfile)
    return Preferences
    


def Main():
    CurrentTime = datetime.datetime.now()
    CurrentHour = CurrentTime.hour
    CurrentMin = CurrentTime.minute

    DataBaseSizeOf = MemSwap('MasterPool.db')
    MasterPool = str("MasterPool.db")

    while CurrentHour == 0 and CurrentMin <= 0 and CurrentMin >= 15:
        try:
            ProcessorNodesActive = []
            ProcessorNodePossible = os.cpu_count()
            PoolResult = Array('i',DataBaseSizeOf.GetPoolSize())
            for ProcessSetIterator_I in range(ProcessorNodePossible):
                poolNode = Process(target = poolBuild, args = (MasterPool,PoolResult,))
                ProcessorNodesActive.append(poolNode)
            for eachProcess in ProcessorNodesActive:
                eachProcess.start()
            for eachProcess in ProcessorNodesActive:
                eachProcess.join()
            for eachProcess in ProcessorNodesActive:
                eachProcess.close()
        except ProcessError:
            print("Fatal processing error>>> Killing...")
            break
    
    ActiveStocks = PoolResult[:]

    while CurrentHour == 6 and CurrentMin != 59:
        try:
            TrendlineTrack(ActiveStocks)
        except IndexError:
            break
            print("Fatal error: Ending all processes")
            
#Settings definition and mutual use
Preferences = getParameters("ProfileSettings.json")
CurrentProfile = JSONSettings(list(Preferences))


#Database Memory Share
DataBaseSizeOf = MemSwap('MasterPool.db')
MasterPool = str("MasterPool.db")

if __name__ == "__main__":
    if CurrentProfile.MasterArm == bool(True):
        Main()
    else:
        try:
            ProcessorNodesActive = []
            ProcessorNodePossible = os.cpu_count()
            PoolResult = Array('i',DataBaseSizeOf.GetPoolSize())
            for ProcessSetIterator_I in range(ProcessorNodePossible):
                poolNode = Process(target = poolBuild, args = (MasterPool,PoolResult,))
                ProcessorNodesActive.append(poolNode)
            for eachProcess in ProcessorNodesActive:
                eachProcess.start()
            for eachProcess in ProcessorNodesActive:
                eachProcess.join()
            for eachProcess in ProcessorNodesActive:
                eachProcess.close()
        except ProcessError:
            print("Fatal processing error>>> Killing...")
import sqlite3 as dbase
import yfinance as charts
import datetime 
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
import math
import time
import threading
import concurrent
import os 
from MemSwap import MemSwap
from MACD import MACD,WhereCross
import json
from Settings import JSONSettings
import stockstats
from ThreadHandler import Queue
import hashlib
import sys
import multiprocessing

global stack

#Initialize the main stack
stack = Queue()


#Set home
CurrentDirectory = os.path.dirname(os.path.abspath(__file__))
os.chdir(CurrentDirectory)      

#Move stocks from database to active list
def poolBuild(database,Verbose):
    pool = []
    init = dbase.connect(str(database))
    Connection = init.Connection()
    for row in Connection.execute("SELECT * FROM ActivePool"):
        try:
            if row[1] == int(1):
                if Verbose == True:
                    print('Adding '+ str(row[0]))
                else:
                    pass
                pool.append(str(row[0]))
        except IndexError:
            break
           

def TrendlineTrack(stock,Verbose):
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

        if Verbose == True:
            print("Data for " + str(stock)+":\n")
            print(PairedData)
        else:
            pass

        
        CurrentStock = MACD(stockData)
        SignalLineValues = CurrentStock.getSignalLineValues()
        MACDValues = CurrentStock.getMACDValues()

        SignalSet = WhereCross(byday = list(range(0,9)), macd_vals = MACDValues, signal_vals = SignalLineValues)
        MarkedEvents = SignalSet.do()

        BuyIndications = MarkedEvents[0]
        SellIndications = MarkedEvents[1]
        StrongBuyIndication = MarkedEvents[2]


    except IndexError:
        sys.exit("IndexError: Fatal>>> Closing...") 
        

def getParameters(SettingsFile): 
    with open(str(SettingsFile),'r') as SettingsProfile:
        Preferences = json.load(SettingsProfile)
    return Preferences

        

if __name__ == "__main__":

    #Load settings
    Preferences = getParameters("ProfileSettings.json")
    CurrentProfile = JSONSettings(dict(Preferences))


    print("Welcome to Trender" + str(CurrentProfile.ProfileName) + "please sign in\n")
    UsernamePreAuth = str(input("Username:"))
    print("\n")
    PasswordPreAuth = str(input("Password:"))
    print("\n")
    
    UsernameCipher = hashlib.sha256(UsernamePreAuth.encode())
    PasswordCipher = hashlib.sha256(PasswordPreAuth.encode())
    #--------------------------------
    #----DB-Data---------------------
    seqfmtu = (str(UsernamePreAuth,))
    seqfmtp = (str(PasswordCipher,))
    #--------Grab-password-----------
    try:
        OpenConnection = dbase.connect('users.db')
        Connection = OpenConnection.Connection()
        Connection.execute("SELECT * FROM UserData WHERE username=?",(seqfmtu,))
        DBResults = Connection.fetchall()
        FoundData = DBResults[0]
        PasswordOnFile = FoundData[1]
    except:
        print("Database Error!")
        sys.exit()
    #--------------------------------
    if PasswordCipher.hexdigest() == PasswordOnFile:
        Connection.close()
    else:
        print("Authentication Error!")
        sys.exit()


    if CurrentProfile.MasterArm == bool(True):
        CurrentTime = datetime.datetime.now()
        CurrentHour = CurrentTime.hour
        CurrentMin = CurrentTime.minute

        if stack.MaxCores != CurrentProfile.MaximumThreadsAllowed:
            sys.exit("Current ProfileSettings.json configuration not compatable with this CPU \n insufficient threads")


        while CurrentHour == 0 and CurrentMin >= 0 and CurrentMin <= 15:
                try:
                    PoolReturns = list(poolBuild(CurrentProfile.DefaultDatabase,CurrentProfile.Verbose))
                except IndexError:
                    pass


        TraceReturns = []
        while CurrentHour == 6 and CurrentMin != 59:
            with concurrent.futures.ThreadPoolExecutor() as excecutor:
                for StockIndex in range(0,len(PoolReturns),stack.MaxCores):
                        if stack.MaxCores == 1:
                            TraceReturns.append(TrendlineTrack(PoolReturns[StockIndex],CurrentProfile.Verbose))
                        
                        elif stack.MaxCores == 2:
                            Thread1 = excecutor.submit(fn=TrendlineTrack, args=(PoolReturns[StockIndex],CurrentProfile.Verbose))
                            Thread2 = excecutor.submit(fn=TrendlineTrack, args=(PoolReturns[StockIndex + 1],CurrentProfile.Verbose))

                            stack.place(Thread1.result())
                            stack.place(Thread2.result())
                        
                        elif stack.MaxCores == 8:
                            Thread1 = excecutor.submit(fn=TrendlineTrack, args=(PoolReturns[StockIndex],CurrentProfile.Verbose))
                            Thread2 = excecutor.submit(fn=TrendlineTrack, args=(PoolReturns[StockIndex + 1],CurrentProfile.Verbose))
                            Thread3 = excecutor.submit(fn=TrendlineTrack, args=(PoolReturns[StockIndex + 2],CurrentProfile.Verbose))
                            Thread4 = excecutor.submit(fn=TrendlineTrack, args=(PoolReturns[StockIndex + 3],CurrentProfile.Verbose))
                            Thread5 = excecutor.submit(fn=TrendlineTrack, args=(PoolReturns[StockIndex + 4],CurrentProfile.Verbose))
                            Thread6 = excecutor.submit(fn=TrendlineTrack, args=(PoolReturns[StockIndex + 5],CurrentProfile.Verbose))
                            Thread7 = excecutor.submit(fn=TrendlineTrack, args=(PoolReturns[StockIndex + 6],CurrentProfile.Verbose))
                            Thread8 = excecutor.submit(fn=TrendlineTrack, args=(PoolReturns[StockIndex + 7],CurrentProfile.Verbose))
                        
            


                
                
                
    else:
        sys.exit("Master arm set to false in ProfileSettings.json")
    
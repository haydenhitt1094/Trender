import sqlite3 as dbase
import yfinance as charts
import datetime 
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
import math
import time
import threading
import os 
from MemSwap import MemSwap
from MACD import MACD,WhereCross
import json
from Settings import JSONSettings
import stockstats
from ThreadHandler import Queue
import hashlib
import sys

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
                stack.place(pool)
        except IndexError:
            break
           

def TrendlineTrack(actives,Verbose):
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
            print("IndexError: Fatal>>> Closing...") 
            break


def getParameters(SettingsFile): 
    with open(str(SettingsFile),'r') as SettingsProfile:
            Preferences = json.load(SettingsProfile)
    return Preferences
    
        



if __name__ == "__main__":

    #Load settings
    Preferences = getParameters("ProfileSettings.json")
    CurrentProfile = JSONSettings(list(Preferences))


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

        while CurrentHour == 0 and CurrentMin >= 0 and CurrentMin <= 15:
            try:
                Threads = threading.Thread(target=poolBuild , args=(CurrentProfile.DefaultDatabase,CurrentProfile.Verbose))
                Threads.start()
                
                #Paging for data to finish processing

                while True:
                    Page = stack.isEmpty()
                    if Page:
                        pass
                    else:
                        PoolReturn = list(stack.cut())
                        break

            except IndexError:
                pass


        
        ActiveStocks = PoolReturn

        while CurrentHour == 6 and CurrentMin != 59:
            try:
                Threads = threading.Thread(target=TrendlineTrack, args=(PoolReturn,CurrentProfile.Verbose,))
                Threads.start()


            except:
                break
    else:
        sys.exit("Master arm set to false in ProfileSettings.json")
    
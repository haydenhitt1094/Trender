import json
import multiprocessing
import sys
import os

class JSONSettings:
    def __init__(self,SettingsConstructor):
        self.dirHome = os.curdir
        self.hasIssue = bool(False)
        self.withCode = None
        self.warning = None
        self.MasterArm = bool(SettingsConstructor["MasterArm"])
        self.MaxDollarInvestment = int(SettingsConstructor["MaxInvestment"])
        self.MaxSharesInvestment = int(SettingsConstructor["MaxInvestmentShares"])
        self.FractionalEnabled = bool(SettingsConstructor["FractionalEnabled"])
        self.SellEnabled = bool(SettingsConstructor["SellEnabled"])
        self.BuyEnabled = bool(SettingsConstructor["BuyEnabled"])
        self.ProfileType = SettingsConstructor["Profile"]
        self.Verbose = bool(SettingsConstructor["Verbose"])
        self.MaximumThreadsAllowed = int(SettingsConstructor["MaximumThreadsAllowed"])
        self.DefaultDatabase = str(SettingsConstructor["DefaultDatabase"])
        self.ProfileName = str(SettingsConstructor["ProfileName"])
        self.TimeStudyPeriod = int(SettingsConstructor["TimeStudyPeriod"])
        self.CollectStats = bool(SettingsConstructor["CollectStatistics"])

    def verifySettings(self):
        if int(self.MaximumThreadsAllowed) != int(multiprocessing.cpu_count()):
            self.hasIssue = True
            self.withCode = str("ThreadError")
        
        if self.BuyEnabled == False and self.SellEnabled == False:
            self.withCode = str("EffectivelyDisabledError")
            self.hasIssue = True 
        
        files = []
        for file in os.listdir(os.getcwd()):
            files.append(str(file))
            
        if str(self.DefaultDatabase) not in files:
            self.withCode = str("DatabaseDNE Error")
            self.hasIssue = True
        
        if self.CollectStats == False:
            self.warning = str("Warning: Stats not enabled")


        if self.hasIssue == True and self.warning != None:
            return sys.exit("{}{}".format(self.withCode,self.warning))
        elif self.hasIssue == True and self.warning == None:
            return sys.exit("{}".format(self.withCode)) 
        elif self.hasIssue == False and self.warning != None:
            return sys.exit("{}".format(self.warning))
        else:
            return print(str("Settings validated"))

    def setProfile(self):
        if self.ProfileType == None:
            self.ProfileType == None
            return self.ProfileType
        else:
            self.ProfileType = str(self.ProfileType.lower())
            

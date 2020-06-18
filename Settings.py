import json

class JSONSettings:
    def __init__(self,SettingsConstructor):
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
    def setProfile(self):
        if self.ProfileType == None:
            self.ProfileType == None
            return self.ProfileType
        else:
            self.ProfileType = str(self.ProfileType.lower())
            

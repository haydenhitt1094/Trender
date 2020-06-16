import json

class JSONSettings:
    def __init__(self,SettingsConstructor):
        self.MasterArm = bool(SettingsConstructor[0])
        self.MaxDollarInvestment = int(SettingsConstructor[1])
        self.MaxSharesInvestment = int(SettingsConstructor[2])
        self.FractionalEnabled = bool(SettingsConstructor[3])
        self.SellEnabled = bool(SettingsConstructor[4])
        self.BuyEnabled = bool(SettingsConstructor[5])
        self.ProfileType = SettingsConstructor[6]
    def setProfile(self):
        if self.ProfileType == None:
            self.ProfileType == None
            return self.ProfileType
        else:
            self.ProfileType = str(self.ProfileType.lower())
            

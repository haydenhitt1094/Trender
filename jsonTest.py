import json
from Settings import JSONSettings

def getParameters(SettingsFile): 
    with open(str(SettingsFile),'r') as SettingsProfile:
            Preferences = json.load(SettingsProfile)
    return Preferences

Preferences = getParameters("ProfileSettings.json")
print (Preferences["MasterArm"])
#CurrentProfile = JSONSettings(list(Preferences))




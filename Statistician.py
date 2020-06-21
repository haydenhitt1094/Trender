class Transaction:
    def __init__(self,symbol,shareprice,amount):
        self.entryDeck = []
        self.symbol = symbol
        self.shareprice = shareprice
        self.amount = amount
        self.costbasis = self.amount * self.shareprice
        self.isWriting = False
       
    def submitPurchase(self):
        import json
        import datetime

        self.isWriting = True
        originalContent = []
        try:
            for entry in json.load(open(r"Logs\Transactions.json","r")):
                originalContent.append(entry)
        except:
            pass
        originalContent.append(dict({str(self.symbol):{"Stock":self.symbol,"Shareprice":self.shareprice,"Amount":self.amount,"Costbasis":self.costbasis,"Type":"Purchase","Date":str(datetime.date.today())}}))
        json.dump(originalContent,open(r"Logs\Transactions.json",'w'),indent=4)
        self.isWriting = False
        return print("Transactions list updated with data of: " + str(self.symbol))

    def submitSale(self):
        import json
        import datetime
        self.isWriting = True
        originalContent = []
        try:
            for entry in json.load(open(r"Logs\Transactions.json","r")):
                originalContent.append(entry)
        except:
            pass
        originalContent.append(dict({str(self.symbol):{"Stock":self.symbol,"Shareprice":self.shareprice,"Amount":int(self.amount),"Returns":int(self.costbasis),"Type":"Sale","Date":str(datetime.date.today())}}))
        json.dump(originalContent,open("Transactions.json",'w'),indent=4)
        self.isWriting = False
        return print("Transactions list updated with data of: " + str(self.symbol))

class Statistics:
        
    def __init__(self,alltimelog):
        self.alltimelog = str(alltimelog)

    def updateStats(self):
        import json
        import datetime
        
        
        with open(r"Logs\CurrentHoldings.txt","w") as log:
            log.write("")
        log.close()

        foundResults = []
        transactions = json.load(open(r"Logs\Transactions.json",'r'))
        
        symbols = []

        for line in open(str(self.alltimelog),"r"):
            line2 = line.strip()
            symbols.append(str(line2))
        
        
        for symbol in symbols:
            for jsonIndex in range(len(transactions)):
                try:
                    entry = transactions[jsonIndex][str(symbol)]
                    foundResults.append(entry)
                except:
                    pass
        
        for symbol in symbols:
            ondeck = []
            stocktotal = 0
            for result in foundResults:
                if str(result["Symbol"]) == str(symbol):
                    ondeck.append(result)
                else:
                    pass
            for receipt in ondeck:
                if receipt["Type"] == "Sale":
                    stocktotal = stocktotal + int(receipt["Returns"])
                elif receipt["Type"] == "Purchase":
                    stocktotal = stocktotal - int(receipt["Costbasis"])

            with open(r"Logs\CurrentHoldings.txt","a") as UpdatedStats:
                UpdatedStats.write(str(symbol) + ": $" + str(stocktotal))
            UpdatedStats.close()

class RobinhoodStatistic:
    
    def __init__(self,CurrentHoldingsFile,encryptedCredentials):
    
        self.CurrentHoldingsFile = str(r"Logs\\" + str(CurrentHoldingsFile))
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        self.baseurl = str("")
        self.encryptedCredentials = str(encryptedCredentials)

    def fetchStats(self):
        from bs4 import BeautifulSoup
        import hashlib
        import requests 
        



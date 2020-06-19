class StatsKeeper:
    def __init__(self,symbol,shareprice,amount):
        self.entryDeck = []
        self.symbol = symbol
        self.shareprice = shareprice
        self.amount = amount
        self.costbasis = self.amount * self.shareprice
        self.isWriting = False
       
    def submit(self):
        import json
        self.isWriting = True
        originalContent = []
        try:
            for entry in json.load(open("Transactions.json","r")):
                originalContent.append(entry)
        except:
            pass
        originalContent.append(dict({str(self.symbol):{"Shareprice":self.shareprice,"Amount":self.amount,"Costbasis":self.costbasis}}))
        json.dump(originalContent,open("Transactions.json",'w'),indent=4)
        self.isWriting = False
        return str("Transactions list updated")

    def retrieve_all(self):
        foundResults = []
        transactions = json.load(open("Transactions.json",'r'))
        
        for jsonIndex in range(len(transactions)):
            try:
                entry = transactions[jsonIndex][str(self.symbol)]
                foundResults.append(entry)
            except:
                pass
        return foundResults
    
    def updateHistory(self):
        with open()


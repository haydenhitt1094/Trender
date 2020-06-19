class StatsKeeper:
    def __init__(self,symbol,shareprice,amount):
        self.entryDeck = []
        self.symbol = symbol
        self.shareprice = shareprice
        self.amount = amount
        self.costbasis = self.amount * self.shareprice
       
    def submit(self):
        import json
        originalContent = []
        try:
            for item in json.load(open("Holdings.json","r")):
                originalContent.append(item)
        except:
            pass
        originalContent.append(dict({str(self.symbol):{"Shareprice":self.shareprice,"Amount":self.amount,"Costbasis":self.costbasis}}))
        json.dump(originalContent,open("Holdings.json",'w'),indent=4)
        return str("Done")


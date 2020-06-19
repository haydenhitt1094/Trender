import json

symbol = 00
stock = 0
shareprice = 4
amount = 3
costbasis = 22

originalContent = []
newContent = []

#json.dump(originalContent,open("Holdings.json","w"))

#try:
    #for item in json.load(open("Holdings.json","r")):
        #originalContent.append(item)
#except:
    #pass

#originalContent.append(dict({str(symbol):{"Shareprice":shareprice,"Amount":amount,"Costbasis":costbasis}}))

#json.dump(originalContent,open("Holdings.json",'w'),indent=4)

memoryDump = []

transactions = json.load(open("Transactions.json",'r'))


for i in range(len(transactions)):
    try:
        next1 = transactions[i]["69"]["Amount"]
        print(next1)
    except:
        pass


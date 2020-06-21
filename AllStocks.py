class AllStocks:

    def __init__(self,activeslist,output_target):
        self.output_target = str(output_target)
        self.activeslist = list(activeslist)

    def updateAll(self):
        
        currentlist = []
        for line in open(self.output_target,"r"):
            currentlist.append(line)
        


        additions = []
        for stock in self.activeslist:
            if stock not in currentlist:
                additions.append(stock)
            else:
                pass
        
        with open(self.output_target,"w") as file:
            for addIndex in range(len(additions)):
                file.writelines(additions[addIndex] + "\n")
        
        file.close()
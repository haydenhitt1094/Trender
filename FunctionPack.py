class DirectoryBoiler:
    def __init__(self,file):
        self.file = file
    def setCurrent(self):
        import os as system
        sourceloc = system.path.dirname(system.path.abspath(self.file))
        if system.getcwd() == sourceloc:
            pass
        else:
            print("Working directory successfully modifed")
            system.chdir(sourceloc)

class StockFetch:
    def __init__(self,symbol,shares):
        self.head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
        self.symbol = symbol.upper()
        self.shares = shares
        self.url = str("https://finance.yahoo.com/quote/"+symbol+"?p="+symbol+".tsrc=fin-srch")    
    def getPosition(self):
        from bs4 import BeautifulSoup
        import requests
        callback = requests.get(self.url,headers=self.head)
        parsedhtml = BeautifulSoup(callback.content,'lxml')
        position = parsedhtml.find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
        amount = position.get_text()
        finalamt = float(amount)*int(self.shares)
        return finalamt


class VersionEXE:
    def __init__(self,exefile,debug):
        self.target = exefile
        self.debug = bool(debug)
    def cmdGo(self):
        if self.debug == bool(True):
            pass
        elif self.debug == bool(False):
            import os
            from FunctionPack import DirectoryBoiler
            thisfile = DirectoryBoiler(__file__)
            os.system("pyinstaller --onefile {}".format(self.target))
            print("Success")
        else:
            import tkinter
            root = tkinter.Tk()
            root.title("VersionEXE Error")
            root.geometry("100x100")
            deslab = tkinter.Label(master=root, text= "Error: Debug value not present")

class ProxyCycle:
    def __init__(self, getUrl, cycle):
        from random import choice
        self.getUrl = str(getUrl)
        self.cycle = bool(cycle)
    def initCycle(self):
        import requests
        from bs4 import BeautifulSoup
        addrs = []
        ports = []
        r = requests.get(self.getUrl)
        soup = BeautifulSoup(r.content, 'html5lib')
        address = soup.find_all('td')[::8]
        port = soup.find_all('td')[1::8]
        for addr in address:
            addrs.append(addr)
        for prt in port:
            ports.append(prt)
        zip(addrs,ports)


       

class Test:
    a=1
    def __init__(self,b):
        self.b = b
    
    @classmethod
    def changea(cls,newa):
        cls.a = newa

objekt = Test(10)
#print(objekt.b)
#print(Test.a)
#print(Test.a)
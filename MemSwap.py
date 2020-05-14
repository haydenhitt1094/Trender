class MemSwap:
    def __init__(self,MetaPool):
        self.MetaPool = str(MetaPool)
    def GetPoolSize(self):
        import sqlite3 as dbase
        pool = []
        init = dbase.connect(str(self.MetaPool))
        cursor = init.cursor()
        for row in cursor.execute("SELECT * FROM ActivePool"):
            try:
                if row[1] == int(1):
                    pool.append(str(row[0])) 
                else:
                    pass
            except IndexError:
                break
        return int(len(pool))
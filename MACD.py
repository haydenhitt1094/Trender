class MACD:
    def __init__(self,DataFrame):
        import stockstats
        self.DataFrame = DataFrame
        self.MACDdata = stockstats.StockDataFrame.retype(DataFrame)
    def getMACDValues(self):
        MacdValues = []
        MACDMain = self.MACDdata['macd']
        for DayMACD in range(len(self.MACDdata)):
            MacdValues.append(MACDMain[DayMACD])
        return MacdValues
    def getSignalLineValues(self):
        SignalLineValues = []
        SignalLineMain = self.MACDdata['macds']
        for SingnalLineDay in range(len(self.MACDdata)):
            SignalLineValues.append(SignalLineMain[SingnalLineDay])
        return SignalLineValues


class WhereCross:
    def __init__(self,byday,macd_vals,signal_vals):
        self.macd_vals = macd_vals
        self.signal_vals = signal_vals
        self.byday = byday
    def do(self):
        BuyZone = []
        SellZone = []
        StrongIndicationsBuy = []
        for MACDDay in self.byday:
            try:
                if self.macd_vals[MACDDay] <= self.signal_vals [MACDDay] and self.macd_vals[MACDDay + 1] >= self.signal_vals[MACDDay + 1]:
                    BuyZone.append(MACDDay)
                    if self.macd_vals[MACDDay] < 0 and self.signal_vals[MACDDay] < 0:
                        StrongIndicationsBuy.append(MACDDay)
                    else:
                        pass
                else:
                    pass
            except IndexError:
                pass
        for MACDDay in self.byday:
            try:
                if self.macd_vals[MACDDay] >= self.signal_vals [MACDDay] and self.macd_vals[MACDDay + 1] <= self.signal_vals[MACDDay + 1]:
                    SellZone.append(MACDDay)
                else:
                    pass
            except IndexError:
                pass
        return list(BuyZone,SellZone,StrongIndicationsBuy)


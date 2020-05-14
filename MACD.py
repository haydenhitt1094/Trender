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

class DifferenceGenerator:
    def __init__(self,m_vals,sl_vals,DesiredToleranceDiff):
        self.m_vals = m_vals
        self.sl_vals = sl_vals
        self.DesiredToleranceDiff = DesiredToleranceDiff
    def CalcDifference(self):
        PointsOfInflection = []
        for eachDayMACD in range(len(self.m_vals)):
            if abs(self.m_vals[eachDayMACD] - self.sl_vals[eachDayMACD]) <= self.DesiredToleranceDiff:
                PointsOfInflection.append(eachDayMACD)
            else:
                pass
        return PointsOfInflection


class WhereCross:
    def __init__(self,byday,macd_vals,signal_vals):
        self.macd_vals = macd_vals
        self.signal_vals = signal_vals
        self.byday = byday
    def getWhereCross(self):
        from scipy import interpolate
        

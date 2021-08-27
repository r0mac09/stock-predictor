import yfinance as yf

from excetions import Stock_NoData


class StockPuller:
    def __init__(self):
        pass

    def pull(self, token, start, end):
        tickerData = yf.Ticker(token)
        tickerDf = tickerData.history(interval='1d', start=start, end=end)

        if tickerDf.empty:
            raise Stock_NoData(token)
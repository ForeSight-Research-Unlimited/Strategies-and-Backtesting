import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.widgets as mplw
from matplotlib.backends.backend_pdf import PdfPages, FigureCanvasPdf
import yfinance as yf
import datetime
import csv
import os
import code
import time
from dateutil.relativedelta import relativedelta
from pandas import ExcelWriter
import inline
import traceback

import os
import sys

sys.path.append("..")
import code

print(os.getcwd())

import Project1.data_functions.get_data as getData
import Project1.data_functions.get_indicators as getIndicators
import Project1.graphing_functions.drawer as drawer
import Project1.graphing_functions.plotPortfolio as plotPortfolio

strat_name = 'bollinger_band'

tickerName = "TATAMOTORS.NS"
periodTested = "5y"

data1 = getData.tickerData(symbol= tickerName, period= periodTested)
data1["Typical"] = (data1["Close"] + data1["High"] + data1["Low"])/3



dmaIntv = [3, 5, 10, 25, 50, 100, 200, 500]
emaIntv = [3, 5, 10, 25, 50, 100, 200, 500]


data1DMA = getIndicators.getDMA(data1, dmaIntv)
data1EMA = getIndicators.getEMA(data1, emaIntv)
data1BB = getIndicators.getBB(data1)
data1RSI = getIndicators.getRSI(data1)
data1DMAslope = data1DMA.diff()


portfolio = pd.DataFrame(columns=['Value'])
initialCash = 1e8

currCash = 5*(1e7)
currInvested = 0
assetNum = (5*(1e7))/data1["Typical"].iloc[0]

feesFactor = 0.05

daysBought = np.array([])
daysSold = np.array([])



#"""

for ind in data1.index:

    #markerPrice = data1DMA["DMA3"].loc[ind]
    markerPrice = data1["Typical"].loc[ind]

    #"""

    if( markerPrice > data1BB["1STDUP"].loc[ind] ):

        numCanBuy = ((0.1)*(currCash))/(data1["Typical"].loc[ind])

        currCash -= numCanBuy*data1["Typical"].loc[ind] - min(20, (numCanBuy*data1["Typical"].loc[ind])*feesFactor)
        assetNum += numCanBuy
        daysBought = np.append(daysBought, ind)
    
    elif ( markerPrice < data1BB["1STDDN"].loc[ind]) :

        numCanSell = (assetNum)*0.1

        currCash += numCanSell*data1["Typical"].loc[ind] - min(20, (numCanSell*data1["Typical"].loc[ind])*feesFactor)
        assetNum -= numCanSell
        daysSold = np.append(daysSold, ind)

    

    #"""


    """
    if( markerPrice < data1BB["2STDDN"].loc[ind] ):

        shortMadeCount += 1 

        shortNum += ((0.01)*(currCash))/(data1["Typical"].loc[ind])
        currCash += shortNum*(data1["Typical"].loc[ind])

    elif ( markerPrice > data1BB["1STDDN"].loc[ind] and shortNum > 0 ) :

        shortSoldCount += 1
        currCash -= shortNum*(data1["Typical"].loc[ind])
        shortNum = 0
        
    #"""

    portfolio.loc[ind] = currCash + assetNum*data1["Typical"].loc[ind]




plotPortfolio.plot(data1, tickerName, periodTested, portfolio, strat_name, daysBought, daysSold)



code.interact(local=locals())
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
import Project1.graphing_functions.savePlot as savePlot



def plot(data1, tickerName, periodTested, portfolio, strat_name, daysBought, daysSold):

    fig1 = plt.figure(figsize = (12,12))

    fig1.canvas.set_window_title("%s-%s-%s" %(tickerName, strat_name, periodTested))

    gs1 = fig1.add_gridspec(8,4)

    ax1 = fig1.add_subplot(gs1[0:4,0:4])
    ax1.plot(portfolio.index, portfolio['Value'])
    for it in daysBought:
        ax1.axvline(it, color = 'green', alpha = 0.1)

    for it in daysSold:
        ax1.axvline(it, color = 'red', alpha = 0.1)

    drawer.marginandstuff(portfolio, ax1, fig1)

    ax2 = fig1.add_subplot(gs1[4:8,0:4], sharex = ax1)
    drawer.ohlcplot(data1, ax2, fig1)

    cursor1 = mplw.MultiCursor(fig1.canvas, [ax1,ax2] , horizOn= True , color = "lightskyblue" , linewidth = 1)

    fig1.tight_layout()

    plt.show()

    savePlot.save(portfolio, strat_name, fig1, tickerName, periodTested)

import traceback
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import googlefinance as gf
import nsepy
import code

ticker1 = "^NSEI"
intv = '15m'

yfTicker = yf.Ticker(ticker1)

data1 = pd.DataFrame(yfTicker.history(interval= intv))
#print(data1.head())

#data1.to_csv("/data/%s-%s.csv" %(ticker1, intv))
data1.to_csv("D:\Money-In\Foresight Research\data\%s-%s.csv" %(ticker1, intv))

data1['EMA10'] = data1["Close"].ewm( span = 10 ).mean()
data1['EMA25'] = data1["Close"].ewm( span = 25 ).mean()
data1['EMA50'] = data1["Close"].ewm( span = 50 ).mean()
data1['EMA100'] = data1["Close"].ewm( span = 100 ).mean()
data1['EMA200'] = data1["Close"].ewm( span = 200 ).mean()
data1['EMA500'] = data1["Close"].ewm( span = 500 ).mean()

data1["EMA25-10"] = data1["EMA25"] - data1["EMA10"]
data1["EMA50-25"] = data1["EMA50"] - data1["EMA25"]
data1["EMA100-50"] = data1["EMA100"] - data1["EMA50"]
data1["EMA200-100"] = data1["EMA200"] - data1["EMA100"]




print(data1.tail())

code.interact(local=locals())

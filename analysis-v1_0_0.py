import traceback
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import googlefinance as gf
import code

ticker1 = "^NSEI"
intv = '15m'

yfTicker = yf.Ticker(ticker1)


data1 = pd.DataFrame(yfTicker.history(interval= intv))

data1.to_csv("ForeSight-Research-Unlimited/ema_convergence_strat/data/%s-%s.csv" %(ticker1, intv))


code.interact(local=locals())

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.widgets as mplw
import matplotlib.figure as mplf
import matplotlib.animation as mplani
import yfinance as yf
import datetime
import csv
import os
import code
import scipy as sp
import scipy.stats as stats
import math
from matplotlib.backends.backend_pdf import PdfPages, FigureCanvasPdf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import time
from dateutil.relativedelta import relativedelta
from pandas import ExcelWriter
import glob
import inline
import tkinter as tk
import pickle
import keyboard
import traceback

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score




print("Statistics and plotting program")




try:
    
    data1name = str("^NSEI") #tickername
    ticker1name = data1name
    ticker1 = yf.Ticker(ticker1name)
    startdate = datetime.date.today() - relativedelta(days = 7) - relativedelta(years = 15)
    enddate = datetime.date.today() + relativedelta(days = 1)

    #startdate = datetime.date(2018, 12, 29)
    #enddate = datetime.date(2021 , 1, 7)


except Exception as exp:
    
    print(exp)
    input()


#### -- Defining Functions -- ####


try:

    def DataNorm(x):
        
        y = x.copy()
        
        y = ( x - x.mean() )/( x.max()-x.min() )
        
        return y

    def DataStand(x):
            
        y = x.copy()
        
        y = (x-x.mean())/(x.std())
        
        return y

    def DataStat(x):
        
        return pd.Series(x.to_numpy()).copy()

    def RangeOf(x):
        
        return ( x.max() - x.min() )

    def AvgRangeOf(x):
        
        return x.sort_values( ascending = False)[0:int(data1size/100)].mean() - x.sort_values( ascending = True).iloc[0:int(data1size/100)].mean()

    def AvgMaxOf(x):
        
        return x.sort_values( ascending = False)[0:int(data1size/100)].mean()

    def AvgMinOf(x):
        
        return x.sort_values( ascending = True)[0:int(data1size/100)].mean()

    def Rolling(x,y):
        
        return x.rolling(window = y)

    def roundup( n ):
        
        # Smaller multiple
        a = (n // magofdata1) * magofdata1
        
        # Larger multiple
        b = a + magofdata1
        
        return b
        
    def rounddown( n ):
        
        # Smaller multiple
        a = (n // magofdata1) * magofdata1
        
        # Larger multiple
        b = a + magofdata1
        
        return a

except Exception as exp:
    
    print(exp)
    input()


#### -- Functions Defined -- ####




try:

    if os.path.isdir("D:\Finance\Stocks\Company Data\Recent\%s" %(ticker1name) ) :
        
        pass

    else:

        os.mkdir("D:\Finance\Stocks\Company Data\Recent\%s" %(ticker1name) )


except Exception as exp:
    
    print(exp)
    input()



#### -- Basic Variables -- ####



try:

    print("\n\n\n\nThe Stock in analysis is %s\n\n\n\n" %(data1name))

except Exception as exp:
    
    print(exp)
    input()




try:

    data1loc = str("D:\Finance\Stocks\Company Data\Recent\%s\%s-%s-%s.csv" %( ticker1name , ticker1name , startdate , enddate ) )
    data1 = pd.read_csv( "%s" %(data1loc) )
    data1 = data1.replace( to_replace = float(0), method = 'bfill')
    
    k = []
    
    for i in range(0,len(data1.index)):
        k.append(i)
    
    
    """
    data1["IndexNumbers"] = k
    
    data1.index = data1["IndexNumbers"]
    #"""
    
    
    #"""
    data1.index = data1["Date"]
    data1 = data1.loc[:, data1.columns != "Date"].astype(float)
    data1 = data1.fillna(0)
    data1kindex = data1.index.values
    loda = np.array([])
    for i in data1kindex:
        i = pd.to_datetime(i).date()
        loda = np.append(loda,i)
    data1.index = loda
    
    data1 = data1.loc[startdate:enddate,:]
    #"""
    
    
    print("\n\n\n")
    print("Dataset from %s to %s: \n%s\n\n\n" %(startdate , enddate , data1) )
    
    
except Exception as exp:
    
    print(exp)
    print("Error occured, gathering data online.")
    
    data1 = pd.DataFrame( ticker1.history( start = startdate , end = enddate ) )
    data1kindex = data1.index.values
    loda = np.array([])
    for i in data1kindex:
        i = pd.to_datetime(i).date()
        loda = np.append(loda,i)
    data1.index = loda
    data1 = data1.loc[startdate:enddate,:]
    data1size = len(data1.index)
    
    print("Dataset from %s to %s: \n%s\n\n\n" %(startdate , enddate , data1) )

    """

    for f in glob.glob("D:\Finance\Stocks\Company Data\Recent\%s\%s-*.*"%( ticker1name , ticker1name)):
        os.remove(f)

    """

    pd.DataFrame( ticker1.history( start = startdate , end = enddate ) ).to_csv("D:\Finance\Stocks\Company Data\Recent\%s\%s-%s-%s.csv" %( ticker1name , ticker1name , startdate , enddate ) )

try:

    data1_5yr = pd.read_csv(str("D:\Finance\Stocks\Company Data\Recent\%s\%s-%s-5y.csv" %( ticker1name , ticker1name , startdate) ))
    
    data1_5yr.index = data1_5yr["Date"]
    data1_5yr = data1_5yr.loc[:, data1_5yr.columns != "Date"].astype(float)
    data1_5yr = data1_5yr.fillna(0)
    data1_5yrkindex = data1_5yr.index.values
    loda = np.array([])
    for i in data1_5yrkindex:
        i = pd.to_datetime(i).date()
        loda = np.append(loda,i)
    data1_5yr.index = loda
    
    print("\n\n\n")
    print("Dataset of 5 years = \n" , data1_5yr , "\n\n\n" )

except Exception as exp:
    
    print(exp)
    print("Error occured, gathering data online.")
    data1_5yr = pd.DataFrame( ticker1.history( period = "5Y" ) )
    data1_5yrkindex = data1_5yr.index.values
    loda = np.array([])
    for i in data1_5yrkindex:
        i = pd.to_datetime(i).date()
        loda = np.append(loda,i)
    data1_5yr.index = loda
    print("Dataset  5 year : \n" , data1_5yr , "\n\n\n" )
    
    pd.DataFrame( ticker1.history( period = "5Y" ) ).to_csv("D:\Finance\Stocks\Company Data\Recent\%s\%s-%s-5y.csv" %( ticker1name , ticker1name , startdate) )


try:

    data1size = int(len(data1.index))
    print("Total size of dataset = " , data1size , "\n")
    rangedata = range(0 , data1size)
    start = time.time()
    print("Size of working dataset = " , data1size , "\n \n \n" )
    mnthdates = pd.date_range(startdate,enddate,freq = 'MS')

except Exception as exp:
    
    print(exp)
    input()



#### -- Basic Variables declared -- #



start = time.time()



#### -- Basic Statistics -- ##



try:
    
    print("Basic Statistics : \n\n")
    print("Data mean = \n\n%0.3f\n\n\n" %(data1["Close"].mean()) )
    print("Mean of difference between Open and Close = \n\n%0.3f\n\n\n" %( (data1["Open"] - data1["Close"]).abs().mean() ) )
    print("Standard Deviation of difference between Open and Close = \n\n%0.3f\n\n\n" %( (data1["Open"].abs() - data1["Close"].abs()).std() ) )
    print("Mean of difference of High and Low = \n\n%0.3f\n\n\n" %( (data1["High"] - data1["Low"]).mean() ) )
    print("Standard Deviation of High and Low = \n\n%0.3f\n\n\n" %( (data1["High"] - data1["Low"]).std() ))
    print("Standard Deviation of %s of time period = \n\n%0.3f\n\n\n" %(data1name , data1["Close"].std()) )


    difflow = np.array([])
    diffhigh = np.array([])
    for i,j,k in zip(data1["Close"],data1["Open"],data1["High"]):
        if i > j:
            diffhigh = np.append( diffhigh , (k - i) )
        else:
            diffhigh = np.append( diffhigh , (k - j) )
    avgdiffhigh = np.sum(diffhigh)/len(data1["Close"].index)

    for i,j,k in zip(data1["Close"],data1["Open"],data1["Low"]):
        if i < j:
            difflow = np.append( difflow , (i - k) )
        else:
            difflow = np.append( difflow , (j - k) )
    avgdifflow = np.sum(difflow)/len(data1["Close"].index)

    print("Average distance of O or C from H = %0.3f\nStandard Deviation of O or C from H = %0.3f\n\n\n" %(avgdiffhigh , pd.Series(diffhigh).std() ) )
    print("Average distance of O or C from L = %0.3f\nStandard Deviation of O or C from L = %0.3f\n\n\n" %(avgdifflow , pd.Series(difflow).std() ) )


    data1_ohcl_low_vol = data1
    
    for i in data1.index:
        
        if data1.loc[i,"Volume"] >= (data1["Volume"].mean()):
            
            data1_ohcl_low_vol = data1_ohcl_low_vol.drop(i)
    

    data1_ohcl_high_vol = data1
    
    for i in data1.index:
                
        if data1.loc[i,"Volume"] <= (data1["Volume"].mean()):
            
            data1_ohcl_high_vol = data1_ohcl_high_vol.drop(i)

    print("Data Volume Mean = %0.2f" %(data1["Volume"].mean()))    
    print("Data Low Vol Mean = %0.2f" %(data1_ohcl_low_vol["Volume"].mean()))
    print("Data High Vol Mean = %0.2f" %(data1_ohcl_high_vol["Volume"].mean()))
    
            

except:
    
    print(traceback.print_exc())
    input("\nError BC.\n")



## -- Typical Price -- ##

data1["Typical"] = ((data1["High"] + data1["Low"] + data1["Close"])/3)

## -- RSI -- ##



try:

    pd.options.mode.chained_assignment = None
    
    data1RSI = pd.DataFrame() # columns = data1.columns , index = data1.index )
    data1RSI["Change"] = data1["Close"].copy().diff()
    
    data1RSI["Gain"] = [0]*len(data1["Close"].index)
    data1RSI["Loss"] = [0]*len(data1["Close"].index)
    
    
    for i in data1["Close"].diff().index:
    
        if data1["Close"].diff().loc[i] > 0:
            
            data1RSI["Gain"].loc[i] = data1["Close"].copy().diff().loc[i]
        
        elif data1["Close"].diff().loc[i] < 0:
            
            data1RSI["Loss"].loc[i] = abs(data1["Close"].copy().diff().loc[i])
        
        else:
            
            data1RSI["Gain"].loc[i] = float(0)
            data1RSI["Loss"].loc[i] = float(0)

    data1RSI["Avg Gain"] = data1RSI["Gain"].rolling(window = 14).mean()
    data1RSI["Avg Loss"] = data1RSI["Loss"].rolling(window = 14).mean()
    data1RSI["RS"] = data1RSI["Avg Gain"]/data1RSI["Avg Loss"]
    
    data1RSI["RSI"] = ( 100 - ( 100/(1 + data1RSI["RS"]) ) )


except Exception as exp:
    
    print(exp)
    input()



## -- RSI Done -- ##



## -- EMA - MACD -- ##



try:

    data1MACD = pd.DataFrame()
    sst = 10
    lst = 25
    slt = 50
    llt = 100
    
    data1MACD["EMA %s" %(sst)] = data1["Close"].ewm( span = sst ).mean()
    data1MACD["EMA %s" %(lst)] = data1["Close"].ewm( span = lst ).mean()
    data1MACD["EMA %s" %(slt)] = data1["Close"].ewm( span = slt ).mean()
    data1MACD["EMA %s" %(llt)] = data1["Close"].ewm( span = llt ).mean()

except Exception as exp:
    
    print(exp)
    input()


## -- EMA - MACD Done -- ##





## -- Bollinger Bands -- ##



try:

    data1BB = pd.DataFrame()

    data1BB["1STDUP"] = data1["Typical"].rolling(window = 10).mean() + data1["Typical"].rolling(window = 10).std()
    data1BB["2STDUP"] = data1["Typical"].rolling(window = 10).mean() + 2*(data1["Typical"].rolling(window = 10).std())
    data1BB["1STDDN"] = data1["Typical"].rolling(window = 10).mean() - data1["Typical"].rolling(window = 10).std()
    data1BB["2STDDN"] = data1["Typical"].rolling(window = 10).mean() - 2*(data1["Typical"].rolling(window = 10).std())
    

except Exception as exp:
    
    print(exp)
    input()


















## -- Close Price * Difference -- ##

try:

    data1closediffandvol = data1["Close"].diff()*data1["Volume"]

except Exception as exp:
    
    print(exp)
    input()



## -- Close Price * Difference -- ##



#### -- Basic Statistics done -- ####



#### -- Graphing and plotting -- ####



try:

    lastprice = float(data1["Close"].tail(1))
    magoften = 1 #np.array([1,10,100,1000,10000,100000,1000000,1000000,100000000,1000000000,10000000000,100000000000,1000000000000])
    magofdata1 = 1

    while True:
            
        if int(lastprice/magoften) == 0:
            magofdata1 = magoften
            break
        
        else:
        
            magoften = magoften*10
    
    magofdata1 = magofdata1/100
    
    
except Exception as exp:
    
    print(exp)
    input()



## -- OHLC Chart -- ##



try:

    
    data1ohlc = pd.DataFrame()
    data1ohlc["OmC"] = data1["Open"].copy()
    data1ohlc["CmO"] = data1["Close"].copy()
    data1ohlc["HmO"] = data1["High"].copy()
    data1ohlc["LlC"] = data1["Low"].copy()
    data1ohlc["HmC"] = data1["High"].copy()
    data1ohlc["LlO"] = data1["Low"].copy()
    
        
    for i in data1.index:

        if data1["Open"].loc[i] >= data1["Close"].loc[i]:

            data1ohlc["OmC"].loc[i] = data1["Open"].loc[i] - data1["Close"].loc[i]
            data1ohlc["HmO"].loc[i] = data1["High"].loc[i] - data1["Open"].loc[i]
            data1ohlc["LlC"].loc[i] = data1["Close"].loc[i] - data1["Low"].loc[i]
            data1ohlc["CmO"].loc[i] = int(0)
            data1ohlc["HmC"].loc[i] = int(0)
            data1ohlc["LlO"].loc[i] = int(0)
            
        elif data1["Close"].loc[i] >= data1["Open"].loc[i]:

            data1ohlc["CmO"].loc[i] = data1["Close"].loc[i] - data1["Open"].loc[i]
            data1ohlc["HmC"].loc[i] = data1["High"].loc[i] - data1["Close"].loc[i]
            data1ohlc["LlO"].loc[i] = data1["Open"].loc[i] - data1["Low"].loc[i]
            data1ohlc["OmC"].loc[i] = int(0)
            data1ohlc["HmO"].loc[i] = int(0)
            data1ohlc["LlC"].loc[i] = int(0)


    def ohlcplot(ax):

        ax.bar(data1.index , data1ohlc["OmC"] , bottom = data1["Close"] , color = "red" , width = 0.7)
        ax.bar(data1.index , data1ohlc["CmO"] , bottom = data1["Open"] , color = "green" , width = 0.7)
        
        ax.bar(data1.index , data1ohlc["HmO"] , bottom = data1["Open"] , color = "red" , width = 0.2)
        ax.bar(data1.index , data1ohlc["HmC"] , bottom = data1["Close"] , color = "green" , width = 0.2)

        ax.bar(data1.index , data1ohlc["LlC"] , bottom = data1["Low"] , color = "red" , width = 0.2)
        ax.bar(data1.index , data1ohlc["LlO"] , bottom = data1["Low"] , color = "green" , width = 0.2)


except Exception as exp:
    
    print(exp)
    input()


try:

    def marginandstuff():

        ax = plt.gca()
        fig = plt.gcf()
        
        
        """
        
        ax.set_xlim( -50 , len(data1.index) + 50 )
        ax.set_xticks(data1.index[::10])
        ax.set_xticklabels(data1["Date"].iloc[::10] , rotation = 60 )
        
        #"""
        
        
        #"""
        
        ax.set_xlim(startdate - datetime.timedelta(days = 50) , enddate + datetime.timedelta(days = 50))

        month = mdates.MonthLocator(interval=1)
        month_format = mdates.DateFormatter('%d-%m-%y')
        
        days = mdates.DayLocator(interval=1)
        day_format = mdates.DateFormatter("%d-%m-%y")

        ax.xaxis.grid(True, which = 'major')

        ax.xaxis.set_major_locator(month)
        ax.xaxis.set_major_formatter(month_format)
        
        ax.xaxis.set_minor_locator(days)
        
        fig.autofmt_xdate()
        
        #"""


        for i in np.arange( rounddown(data1["Low"].min() - (data1["Close"].mean()/100)) , roundup(data1["High"].max() + (data1["Close"].mean()/100)) , magofdata1):
            ax.axhline( y = i , linewidth = 0.1 )

        ax.set_ylim( rounddown(data1["Low"].min() - (data1["Close"].mean()/100)) , roundup(data1["High"].max() + (data1["Close"].mean()/100)) )
        ax.set_yticks( np.arange( rounddown(data1["Low"].min() - (data1["Close"].mean()/100)) , roundup(data1["High"].max() + (data1["Close"].mean()/100)) , magofdata1) )


    

    def marginandstuffforx():

        ax = plt.gca()
        fig = plt.gcf()
        
        ax.set_xlim(startdate - datetime.timedelta(days = 50) , enddate + datetime.timedelta(days = 50))

        month = mdates.MonthLocator(interval=1)

        month_format = mdates.DateFormatter('%d-%m-%y')

        ax.xaxis.grid(True, which = 'major')

        ax.xaxis.set_major_locator(month)
        ax.xaxis.set_major_formatter(month_format)
        
        fig.autofmt_xdate()



except Exception as exp:
    
    print(exp)
    input()





try:
    
    
    
    
    
    class Drawer(object):




        def __init__(self,ax,fig):
            
            
            self.ax = ax
            self.fig = fig
            
            self.check_button_line_drawer = mplw.CheckButtons( plt.axes([0.76,0.867,0.10,0.1]) , labels = [" Line Drawer"," Horizontal Line"," Vertical Line"] )
            self.check_button_rect_drawer = mplw.CheckButtons( plt.axes([0.76,0.817,0.10,0.05]) , labels = [" Rectangle\n Drawer"] )
            self.check_button_long_n_short_drawer = mplw.CheckButtons( plt.axes([0.76,0.717,0.10,0.1]) , labels = [" Long Position" , " Short Position"] )
            self.check_button_fib_retrac_drawer = mplw.CheckButtons( plt.axes([0.76,0.667,0.10,0.05]) , labels = [" Fibonacci\n Retracement"] )


            self.check_button_select_regression_points = mplw.CheckButtons( plt.axes([0.76,0.617,0.10,0.05]) , labels = [" Regression Points"] )            
            self.click_button_draw_regresseion_line = mplw.Button( plt.axes([0.76,0.567,0.10,0.05]) , label= " Draw Regression Line")
            self.click_button_draw_regresseion_line.on_clicked(self.draw_regression_line)


            self.click_button_delete_points = mplw.Button( plt.axes([0.76,0.517,0.10,0.05]) , label= " Delete Points")
            self.click_button_delete_points.on_clicked(self.delete_points)
            

            self.check_button_select_return_points = mplw.CheckButtons( plt.axes([0.76,0.467,0.10,0.05]) , labels = [" Return Points"] )
            self.click_button_draw_return_line = mplw.Button( plt.axes([0.76,0.417,0.10,0.05]) , label= " Draw Return Line")
            self.click_button_draw_return_line.on_clicked(self.draw_return_line)


            self.rxs = np.array([])
            self.rys = np.array([])


            self.cid_pick = self.fig.canvas.mpl_connect('pick_event', self.on_pick)
            self.cid_key = self.fig.canvas.mpl_connect('key_press_event', self.on_key)
            
            self.cid_mouse_click_linedrawer = self.fig.canvas.mpl_connect('button_press_event', self.line_drawer)
            self.cid_mouse_click_hori_linedrawer = self.fig.canvas.mpl_connect('button_press_event', self.hori_line_drawer)
            self.cid_mouse_click_veri_linedrawer = self.fig.canvas.mpl_connect('button_press_event', self.veri_line_drawer)
            self.cid_mouse_click_rect_drawer = self.fig.canvas.mpl_connect('button_press_event', self.rect_drawer)
            self.cid_mouse_click_long_posi_drawer = self.fig.canvas.mpl_connect('button_press_event', self.long_posi_drawer)
            self.cid_mouse_click_short_posi_drawer = self.fig.canvas.mpl_connect('button_press_event', self.short_posi_drawer)
            self.cid_mouse_click_fib_retrac_drawer = self.fig.canvas.mpl_connect('button_press_event', self.fib_retrac_drawer)
            self.cid_mouse_click_regression_points = self.fig.canvas.mpl_connect('button_press_event', self.select_regression_point)
            self.cid_mouse_click_return_points = self.fig.canvas.mpl_connect('button_press_event', self.select_return_point)
            
            #self.cid_mouse_click = self.fig.canvas.mpl_connect('button_press_event', self.get_mouse_click)
            #self.cid_mouse_release = self.fig.canvas.mpl_connect('button_release_event', self.get_mouse_release)
            #self.cid_mouse_move = self.fig.canvas.mpl_connect('motion_notify_event', self.get_mouse_move)
            #self.cid_get_key_press = self.fig.canvas.mpl_connect('key_press_event', self.get_key_press)
            #self.cid_get_key_release = self.fig.canvas.mpl_connect('key_press_event', self.get_key_release)
            #self.cid_mouse_enter_axis = self.fig.canvas.mpl_connect('axes_enter_event', self.draw_line)

        def select_return_point(self, event):

            if self.check_button_select_return_points.get_status()[0]:
                
                if event.dblclick:
                    
                    if event.button == 1:
                        
                        print("Getting data : \n")
                        
                        self.rxs = np.append( self.rxs , event.xdata )
                        self.rys = np.append( self.rys , event.ydata )
                        
                        print("X-axis/Dates:")
                        print(self.rxs)
                        print("Y-axis/Price:")
                        print(self.rys)

        
        def draw_return_line(self,event):
            
            if(self.rxs.size == 2):
                
                for itx, ity in zip(self.rxs, self.rys):
                    print("Points at date:%f -  Price:%f" %(itx, ity))

                sttAmt = self.rys[0]
                endAmt = self.rys[1]

                sttDate = self.rxs[0]
                endDate = self.rxs[1]

                numYr = (float)((endDate - sttDate)/365)
                cmpdRate = (float)(( (endAmt/sttAmt)**(1.0/numYr) ) - 1)*100

                print("Compounded annual rate = %f" %(cmpdRate))

                numPricePoints = np.array([])
                numDatePoints = np.array([])

                nPoints = int(endDate - sttDate) + 1

                for i in range(0,nPoints+1):
                    
                    amt = sttAmt*((1+ float(cmpdRate)/100.0)**(i/365.0) )
                    numPricePoints = np.append(numPricePoints, amt)
                    numDatePoints = np.append(numDatePoints, sttDate + i)

                print( "Yeh rahe points: %0.02f , %0.02f " %(numDatePoints[-1], numPricePoints[-1]))

                return_line = self.ax.plot(numDatePoints, numPricePoints, picker=True , pickradius = 5 , color = "blue" , linewidth = 0.8)
                return_line.figure.canvas.draw()

                self.ax.text( numDatePoints[-1], numPricePoints[-1], cmpdRate, fontsize=12, picker = True)
                self.ax.text( 1, 1, cmpdRate, fontsize=100, picker = True)

                self.ax.figure.canvas.draw()

                #self.ax.text( min(event.xdata,xy[0][0]) + 2*( max(event.xdata,xy[0][0]) - min(event.xdata,xy[0][0]) ) , min(event.ydata,xy[0][1]) , "0" , fontsize=10 , picker = True )

                pass

            else:

                print("Invalid points selected, please delete and reselect")





        
        def select_regression_point(self,event):

            if self.check_button_select_regression_points.get_status()[0]:
                
                if event.dblclick:
                    
                    if event.button == 1:
                        
                        print("Getting data : \n")
                        
                        self.rxs = np.append( self.rxs , event.xdata )
                        self.rys = np.append( self.rys , event.ydata )
                        
                        print(self.rxs,"\n",self.rys)


        def draw_regression_line(self,event):
            
            if self.rxs.size != 0:
            
                regr = linear_model.LinearRegression()
                
                self.rxs = np.reshape(self.rxs, (len(self.rxs),1))
                #self.rys = np.reshape(self.rys, (len(self.rys),1))
                
                regr.fit(self.rxs,self.rys)
                
                print(self.rxs,"\n",self.rys)
                print(regr.coef_)
                print(regr.intercept_)
                
                
                pred_rys = regr.predict(self.rxs)
                
                regr_line, = self.ax.plot(self.rxs , pred_rys , picker=True , pickradius = 5 , color = "blue" , linewidth = 0.8)
                regr_line.figure.canvas.draw()
                
                self.rxs = [[]]
                self.rys = [[]]


        def delete_points(self, event):

            self.rxs = np.array([])
            self.rys = np.array([])

        
        
        
        
        
        
        
        
        def line_drawer(self,event):
                    
            
            if self.check_button_line_drawer.get_status()[0]:
                    
                if event.dblclick:
                    
                    if event.button == 1:
                        
                        self.xs = event.xdata
                        self.ys = event.ydata

                        self.cid_mouse_move_line_drawer = self.fig.canvas.mpl_connect('motion_notify_event', self.mouse_move_line_drawer)
                        
                        while True:
                            
                            try:
                                xy = plt.ginput(1)
                                break
                            except:
                                pass
                        
                        self.fig.canvas.mpl_disconnect(self.cid_mouse_move_line_drawer)
                        
                        x = [event.xdata,xy[0][0]]
                        y = [event.ydata,xy[0][1]]
                        line, = self.ax.plot(x , y , picker=True , pickradius = 5 , color = "blue" , linewidth = 0.8)
                        line.figure.canvas.draw()
                    
                        
        def mouse_move_line_drawer(self,event):
            
            if event.inaxes:
                
                line, = self.ax.plot([self.xs , event.xdata], [self.ys , event.ydata], 'r' , linewidth = 0.1 , alpha = 0.7)
                line.figure.canvas.draw()
                self.ax.lines.pop()



        def hori_line_drawer(self,event):
            
            
            if self.check_button_line_drawer.get_status()[1]:

                if event.dblclick:
            
                    line = self.ax.axhline(event.ydata , picker = True , pickradius = 5 , color = "violet" , alpha = 0.5)

                    #mpl.backend_bases.NavigationToolbar2(self.fig.canvas).push_current()
                        
                    self.ax.figure.canvas.draw()
                        
                    if mpl.backend_bases.NavigationToolbar2(self.fig.canvas) is None:
                        pass
                    else:
                        mpl.backend_bases.NavigationToolbar2(self.fig.canvas).back()
        
                else:
                    
                    pass
                
            else:
                    
                pass



        def veri_line_drawer(self,event):
        
            
            if self.check_button_line_drawer.get_status()[2]:

                if event.dblclick:
                    
                    line = self.ax.axvline(event.xdata , picker = True , pickradius = 5 , color = "sienna" , alpha = 0.5)
                    
                    self.ax.figure.canvas.draw()
                else:
                    
                    pass
            else:
                    
                pass
            
            








        def rect_drawer(self,event):
            

            if self.check_button_rect_drawer.get_status()[0]:
                
                if event.dblclick:
                
                    self.xs = event.xdata
                    self.ys = event.ydata
                    
                    self.cid_mouse_move_rect = self.fig.canvas.mpl_connect('motion_notify_event', self.mouse_move_rect_drawer)
                    
                    while True:
                    
                        try:
                            xy = plt.ginput(1)
                            break
                        except:
                            pass
                    
                    self.fig.canvas.mpl_disconnect(self.cid_mouse_move_rect)
                    
                    rectadd = mpl.patches.Rectangle( (min(event.xdata,xy[0][0]) , min(event.ydata,xy[0][1]) ) , 
                                                            np.abs(event.xdata - xy[0][0]) , np.abs(event.ydata - xy[0][1]) ,
                                                            angle = 0.0 , color = "skyblue" , alpha = 0.3 , picker = True)
                    
                    self.ax.add_patch(rectadd)
                    self.ax.figure.canvas.draw()

                    mpl.backend_bases.NavigationToolbar2(self.fig.canvas).push_current()                
                    mpl.backend_bases.NavigationToolbar2(self.fig.canvas).back()

                else:
                    
                    pass
            
            else:
                    
                pass
            
        
        def mouse_move_rect_drawer(self,event):
            
            if event.inaxes:
                            
                rect = mpl.patches.Rectangle( ( min( event.xdata , self.xs ) , min( event.ydata , self.ys ) ) , 
                                                        np.abs(event.xdata - self.xs ) , np.abs(event.ydata - self.ys ) ,
                                                        angle = 0.0 , color = "skyblue" , alpha = 0.3 )
                
                self.ax.add_patch(rect)
                self.ax.figure.canvas.draw()
                
                self.ax.patches.pop()










        def long_posi_drawer(self,event):
            
            
            if self.check_button_long_n_short_drawer.get_status()[0]:
            
                if event.dblclick:
            
                    self.xs = event.xdata
                    self.ys = event.ydata
                    
                    self.ratio = 0.333333333333
                    
                    self.cid_mouse_move_long_posi = self.fig.canvas.mpl_connect('motion_notify_event', self.mouse_move_long_posi_drawer)
                
                    xy = plt.ginput(1)

                    self.fig.canvas.mpl_disconnect(self.cid_mouse_move_long_posi)
                                                        
                    rkrwrectprofper = mpl.patches.Rectangle( ( min( event.xdata , xy[0][0] ) , min( event.ydata , xy[0][1] ) ) , 
                                                            np.abs( event.xdata - xy[0][0] ) , np.abs( event.ydata - xy[0][1] ) ,
                                                            angle = 0.0 , color = "lightgreen" , alpha = 0.3 , picker = True )
                    
                    rkrwrectlossper = mpl.patches.Rectangle( ( min( event.xdata , xy[0][0] ) , min( event.ydata , xy[0][1] ) ) , 
                                                            np.abs( event.xdata - xy[0][0] ) , (-self.ratio)*( np.abs( event.ydata - xy[0][1] ) ) ,
                                                            angle = 0.0 , color = "lightcoral" , alpha = 0.3 , picker = True )
                        
                    self.ax.add_patch(rkrwrectprofper)
                    self.ax.add_patch(rkrwrectlossper)

                    self.ax.figure.canvas.draw()
                    
                    mpl.backend_bases.NavigationToolbar2(self.fig.canvas).push_current()                
                    mpl.backend_bases.NavigationToolbar2(self.fig.canvas).back()
                
                else:
                    
                    pass

            else:
                    
                pass
        
        
        def mouse_move_long_posi_drawer(self,event):
            
            if event.inaxes:
             
                rkrwrectprof = mpl.patches.Rectangle( ( min( event.xdata , self.xs ) , min( event.ydata , self.ys ) ) , 
                                                        np.abs(event.xdata - self.xs ) , np.abs(event.ydata - self.ys ) ,
                                                        angle = 0.0 , color = "lightgreen" , alpha = 0.3 )
                
                rkrwrectloss = mpl.patches.Rectangle( ( min( event.xdata , self.xs ) , min( event.ydata , self.ys ) ) , 
                                                        np.abs(event.xdata - self.xs ) , (-self.ratio)*( np.abs( event.ydata - self.ys ) ) ,
                                                        angle = 0.0 , color = "lightcoral" , alpha = 0.3 )
                
                self.ax.add_patch(rkrwrectprof)
                self.ax.add_patch(rkrwrectloss)
                
                self.ax.figure.canvas.draw()
                self.ax.figure.canvas.draw()

                self.ax.patches.pop()
                self.ax.patches.pop()
        


        def short_posi_drawer(self,event):
        
            
            if self.check_button_long_n_short_drawer.get_status()[1]:
        
                if event.dblclick:
                            
                    self.xs = event.xdata
                    self.ys = event.ydata
                    
                    self.ratio = 0.333333333333
                    
                    
                    self.cid_mouse_move_short_posi = self.fig.canvas.mpl_connect('motion_notify_event', self.mouse_move_short_posi_drawer)

                    xy = plt.ginput(1)

                    self.fig.canvas.mpl_disconnect(self.cid_mouse_move_short_posi)       
                    
                    rkrwrectprofper = mpl.patches.Rectangle( ( min( event.xdata , xy[0][0] ) , min( event.ydata , xy[0][1] ) ) , 
                                                            np.abs( event.xdata - xy[0][0] ) , np.abs( event.ydata - xy[0][1] ) ,
                                                            angle = 0.0 , color = "lightgreen" , alpha = 0.3 , picker = True )
                    
                    rkrwrectlossper = mpl.patches.Rectangle( ( min( event.xdata , xy[0][0] ) , max( event.ydata , xy[0][1] ) ) , 
                                                            np.abs( event.xdata - xy[0][0] ) , (self.ratio)*( np.abs( event.ydata - xy[0][1] ) ) , 
                                                            angle = 0.0 , color = "lightcoral" , alpha = 0.3 , picker = True )
                    
                    self.ax.add_patch(rkrwrectprofper)
                    self.ax.add_patch(rkrwrectlossper)

                    self.ax.figure.canvas.draw()
                    
                    mpl.backend_bases.NavigationToolbar2(self.fig.canvas).push_current()
                    mpl.backend_bases.NavigationToolbar2(self.fig.canvas).back()
                
                
                else:
                    
                    pass

            else:
                    
                pass
        
        
        def mouse_move_short_posi_drawer(self,event):
            
            if event.inaxes:
                
                rkrwrectprof = mpl.patches.Rectangle( ( min( event.xdata , self.xs) , min( event.ydata , self.ys ) ) , 
                                                        np.abs(event.xdata - self.xs ) , np.abs(event.ydata - self.ys) ,
                                                        angle = 0.0 , color = "lightgreen" , alpha = 0.3 )
                
                rkrwrectloss = mpl.patches.Rectangle( ( min( event.xdata , self.xs ) , max( event.ydata , self.ys ) ) , 
                                                        np.abs(event.xdata - self.xs) , (self.ratio)*( np.abs(event.ydata - self.ys) ) ,
                                                        angle = 0.0 , color = "lightcoral" , alpha = 0.3 )
                
                self.ax.add_patch(rkrwrectprof)
                self.ax.add_patch(rkrwrectloss)
                
                self.ax.figure.canvas.draw()
                self.ax.figure.canvas.draw()

                self.ax.patches.pop()
                self.ax.patches.pop()




        
        def fib_retrac_drawer(self,event):
            
            if self.check_button_fib_retrac_drawer.get_status()[0]:
                
                if event.dblclick:
                    
                    
                    self.xs = event.xdata
                    self.ys = event.ydata
                    
                    self.cid_mouse_move_fib_retrac_drawer = self.fig.canvas.mpl_connect('motion_notify_event', self.mouse_move_fib_retrac_drawer)
                    
                    xy = plt.ginput(1)
                    
                    self.fig.canvas.mpl_disconnect(self.cid_mouse_move_fib_retrac_drawer)
                    
                    self.ax.axhline( min(event.ydata,xy[0][1]) , picker = True , pickradius = 5 )
                    self.ax.axhline( min(event.ydata,xy[0][1]) + 0.146*( max(event.ydata,xy[0][1]) - min(event.ydata,xy[0][1]) ) , picker = True , pickradius = 5 )
                    self.ax.axhline( min(event.ydata,xy[0][1]) + 0.236*( max(event.ydata,xy[0][1]) - min(event.ydata,xy[0][1]) ) , picker = True , pickradius = 5 )
                    self.ax.axhline( min(event.ydata,xy[0][1]) + 0.382*( max(event.ydata,xy[0][1]) - min(event.ydata,xy[0][1]) ) , picker = True , pickradius = 5 )
                    self.ax.axhline( min(event.ydata,xy[0][1]) + 0.618*( max(event.ydata,xy[0][1]) - min(event.ydata,xy[0][1]) ) , picker = True , pickradius = 5 )
                    self.ax.axhline( max(event.ydata,xy[0][1]) , picker = True , pickradius = 5 )
                    self.ax.axhline( min(event.ydata,xy[0][1]) + 1.618*( max(event.ydata,xy[0][1]) - min(event.ydata,xy[0][1]) ) , picker = True , pickradius = 5 )
                    
                    self.ax.text( min(event.xdata,xy[0][0]) + 2*( max(event.xdata,xy[0][0]) - min(event.xdata,xy[0][0]) ) , min(event.ydata,xy[0][1]) , "0" , fontsize=10 , picker = True )
                    self.ax.text( min(event.xdata,xy[0][0]) + 2*( max(event.xdata,xy[0][0]) - min(event.xdata,xy[0][0]) ) , min(event.ydata,xy[0][1]) + 0.146*( max(event.ydata,xy[0][1]) - min(event.ydata,xy[0][1]) ) , "0.146" , fontsize=10 , picker = True )
                    self.ax.text( min(event.xdata,xy[0][0]) + 2*( max(event.xdata,xy[0][0]) - min(event.xdata,xy[0][0]) ) , min(event.ydata,xy[0][1]) + 0.236*( max(event.ydata,xy[0][1]) - min(event.ydata,xy[0][1]) ) , "0.236" , fontsize=10 , picker = True )
                    self.ax.text( min(event.xdata,xy[0][0]) + 2*( max(event.xdata,xy[0][0]) - min(event.xdata,xy[0][0]) ) , min(event.ydata,xy[0][1]) + 0.382*( max(event.ydata,xy[0][1]) - min(event.ydata,xy[0][1]) ) , "0.382" , fontsize=10 , picker = True )
                    self.ax.text( min(event.xdata,xy[0][0]) + 2*( max(event.xdata,xy[0][0]) - min(event.xdata,xy[0][0]) ) , min(event.ydata,xy[0][1]) + 0.618*( max(event.ydata,xy[0][1]) - min(event.ydata,xy[0][1]) ) , "0.618" , fontsize=10 , picker = True )
                    self.ax.text( min(event.xdata,xy[0][0]) + 2*( max(event.xdata,xy[0][0]) - min(event.xdata,xy[0][0]) ) , max(event.ydata,xy[0][1]) , "1" , fontsize=10 , picker = True )
                    self.ax.text( min(event.xdata,xy[0][0]) + 2*( max(event.xdata,xy[0][0]) - min(event.xdata,xy[0][0]) ) , min(event.ydata,xy[0][1]) + 1.618*( max(event.ydata,xy[0][1]) - min(event.ydata,xy[0][1]) ) , "1.618" , fontsize=10 , picker = True )
                    
                    self.ax.figure.canvas.draw()
                    
                    pass
            
                else:
                    
                    pass
                
            else:
                    
                pass
            
            
        def mouse_move_fib_retrac_drawer(self,event):
            
            if event.inaxes:


                
                self.ax.axhline( min(event.ydata,self.ys) , picker = True , pickradius = 5 )
                self.ax.axhline( min(event.ydata,self.ys) + 0.146*( max(event.ydata,self.ys) - min(event.ydata,self.ys) ) , picker = True , pickradius = 5 )
                self.ax.axhline( min(event.ydata,self.ys) + 0.236*( max(event.ydata,self.ys) - min(event.ydata,self.ys) ) , picker = True , pickradius = 5 )
                self.ax.axhline( min(event.ydata,self.ys) + 0.382*( max(event.ydata,self.ys) - min(event.ydata,self.ys) ) , picker = True , pickradius = 5 )
                self.ax.axhline( min(event.ydata,self.ys) + 0.618*( max(event.ydata,self.ys) - min(event.ydata,self.ys) ) , picker = True , pickradius = 5 )
                self.ax.axhline( max(event.ydata,self.ys) , picker = True , pickradius = 5 )
                self.ax.axhline( min(event.ydata,self.ys) + 1.618*( max(event.ydata,self.ys) - min(event.ydata,self.ys) ) , picker = True , pickradius = 5 )
                
                self.ax.figure.canvas.draw()
                self.ax.lines.pop()
                self.ax.lines.pop()
                self.ax.lines.pop()
                self.ax.lines.pop()
                self.ax.lines.pop()
                self.ax.lines.pop()
                self.ax.lines.pop()
                
                pass
                        
            pass



























        def on_pick(self,event):

            # the picked object is available as event.artist
            this_artist = event.artist
            
            self.ax.picked_object = this_artist

        


        def on_key(self,event):
                        
            if event.key == u'delete':
                
                if self.ax.picked_object:

                    self.ax.picked_object.remove()
                    self.ax.picked_object = None
                    self.ax.figure.canvas.draw()





        
        
        

        
        
        
        
        
        
        
        
        
        
        
        """
        
        def get_mouse_click(self,event):
            
            
            if not event.inaxes:
                
                return
            
            
            try:
            
                self.mouse_click_loc = [event.xdata,event.ydata]
                self.mouse_click_event = event
            
            except Exception as exp:
                
                print(exp)
                input()


        def get_mouse_release(self,event):
            
            
            if not event.inaxes:
                
                return
            
            
            try:
            
                self.mouse_release = [event.xdata,event.ydata]
            
            except Exception as exp:
                
                print(exp)
                input()

        
        def get_mouse_move(self,event):
        
        
            if not event.inaxes:
                
                return
            
            
            try:            
                
                self.mouse_move = [event.xdata,event.ydata]
            
            except Exception as exp:
                
                print(exp)
                input()

        
        
        def get_key_press(self,event):
        
        
            if not event.inaxes:
                
                return
            
            
            try:
                
                self.key_press_loc = [event.xdata,event.ydata]
                self.key_press = event.key
            
            except Exception as exp:
                
                print(exp)
                input()


        def get_key_release(self,event):
        
        
            if not event.inaxes:
                
                return
            
            
            try:
                
                self.key_release_loc = [event.xdata,event.ydata]
                self.key_release = event.key
            
            except Exception as exp:
                
                print(exp)
                input()


        #"""



except Exception as exp:
    
    print(exp)
    input()




## -- OHLC Chart completed -- ##



## -- Plotting and Charting -- ##




try:



    def plotshowkar():
        plt.show()
        pass



    fig1 = plt.figure(figsize = (12,12))
    gs = fig1.add_gridspec(4,4)
    
    ax101 = fig1.add_subplot(gs[:,0:3])
    ax101.set_title("OHLC chart from %s to %s " %(startdate , enddate))

    ohlcplot(ax101)
    
    marginandstuff()
    
    
        
    fig1.tight_layout()
    
    fig1.canvas.set_window_title("OHLC Chart")
    
    plotkarde101 = Drawer(ax101,fig1)
    
    mcursor1 = mplw.MultiCursor(fig1.canvas , [ax101] , horizOn= True , color = "lightskyblue" , linewidth = 1)


except Exception as exp:

    print(exp)
    input()



end = time.time()
print("Total time taken by program = " , end - start)
print("\n\n\n")



plotshowkar()


    

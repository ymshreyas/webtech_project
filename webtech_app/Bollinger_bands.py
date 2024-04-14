# import futures as ft
import webtech_app.futures as ft
import pandas as pd
from datetime import datetime
import plotly.express as px 
import plotly.graph_objects as go
import random as r
import math as m

global sma
sma = []
stand_dev = []
upper = []
lower = []
def sma_calc(i, ind_vals, days):
    i = i + days - 1
    adder = 0
    for j in range(i, i - days, -1):
        adder = adder + ind_vals[j]

    sma.append(adder/days)

def standard_dev(i, ind_vals, days):
    global sma
    i = i + days - 1
    adder = 0
    for j in range(i, i - days, -1):
        adder = adder + ((ind_vals[j] - sma[-1]) ** 2)

    variance = adder/days
    stand_dev.append(m.sqrt(variance))

def set_up():
    global sma
    sma = []
    global stand_dev
    stand_dev = []
    global upper
    upper = []
    global lower
    lower = []
   
def run(info):
    set_up()
    index = info[0].split()
    line = info[1]
    days = info[2]
    start_date = info[3]
    end_date = info[4]

    # ind = yf.Ticker(index)
    if((index[0] == "NIFTY" or index[0] == "BANKNIFTY" or index[0] == "FINNIFTY") and index[1] == "EQ"):
        ind_history = ft.get_index_prices(index[0], start_date, end_date)
    elif(index[1] == "FUT"):
        ind_history = ft.get_futures_prices(index[0], start_date, end_date)
    elif(index[1] == "EQ"):
        ind_history = ft.get_equity_prices(index[0], start_date, end_date)
    #ind_history = ind.history(start= "2022-09-27", end = "2022-11-26")
    ind_date = pd.Index.tolist(ind_history[line].index)
    ind_vals = [float(ele) for ele in pd.Series.tolist(ind_history[line])]

    print(ind_history)

    ind_open_or = [float(ele) for ele in pd.Series.tolist(ind_history['Open']) ]# open values
    ind_high_or = [float(ele) for ele in pd.Series.tolist(ind_history['High']) ]# high values
    ind_low_or = [float(ele) for ele in pd.Series.tolist(ind_history['Low'])]#low values
    ind_close_or = [float(ele) for ele in pd.Series.tolist(ind_history['Close'])]# close values
    if(index[1] == "FUT"):
        lot_size = [float(ele) for ele in pd.Series.tolist(ind_history['Lot Size'])]
        lot_size = lot_size[-1]
    ind_date = ind_date[days:]
    ind_open = ind_open_or[days:]
    ind_high = ind_high_or[days:]
    ind_low = ind_low_or[days:]
    ind_close = ind_close_or[days:]

    # ind_history = ind_history.drop(['Volume', 'Dividends', 'Stock Splits'],axis = 1)
    # print(type(ind_history))
    # fig = px.line(ind_history, x = ind_history[line].index, y = [ind_history["Open"],ind_history["High"],ind_history["Low"],ind_history["Close"]])#.plot(label='Open')
    fig = go.Figure(data = [go.Candlestick(x = ind_date, open = ind_open, high = ind_high, low = ind_low, close = ind_close)])
    # print(fig.layout.xaxis.range)

    for i in range(0, len(ind_open)):
        try:
            sma_calc(i, ind_vals, days)
            standard_dev(i, ind_vals, days)
            upper.append(sma[-1] + (stand_dev[-1]*2))
            lower.append(sma[-1] - (stand_dev[-1]*2))


        except Exception as e:
            print("Caught in for loop ", e)

      
    fig.add_trace(go.Scatter(x = ind_date, y = sma, name = str(days) + " SMA",line = dict(color = 'blue')))
    fig.add_trace(go.Scatter(x = ind_date, y = upper, name = "Upper Band", line = dict(color = 'green')))
    fig.add_trace(go.Scatter(x = ind_date, y = lower, name = "Lower Band", line = dict(color = 'red')))
    # print(trades )
    fig.show()
    fig.write_html('templates\webtech_app\Bollinger.html')
# run(("NIFTY FUT", "Close", 20, "2021-01-01", "2021-12-31"))
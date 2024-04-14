import webtech_app.futures as ft
# import futures as ft
import pandas as pd
from datetime import datetime
import plotly.express as px 
import plotly.graph_objects as go
import random as r
import random

global ema
ema = []
global total_ema
total_ema = []


def sma_calc(ind_vals, days):
    adder = 0
    for j in range(0, days - 1):
        adder = adder + ind_vals[j]

    ema.append(adder/days)

def ema_calc(i, ind_vals, w):
    try:
        emaofi = (ind_vals[i] * w) + (ema[-1] * (1 - w))
        ema.append(emaofi)
    except Exception as e:
        print("ema_calc error", e)


def set_up():
    global ema
    ema = []
    global total_ema
    total_ema = []
   
def run(info):
    global ema
    global w
    macd = []
    set_up()
    index = info[0].split()
    line = info[1]
    days = max(info[2])
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

    ind_date = ind_date[days-1:]
    ind_open = ind_open_or[days:]
    ind_high = ind_high_or[days:]
    ind_low = ind_low_or[days:]
    ind_close = ind_close_or[days:]

    # ind_history = ind_history.drop(['Volume', 'Dividends', 'Stock Splits'],axis = 1)
    print(type(ind_history))
    # fig = px.line(ind_history, x = ind_history[line].index, y = [ind_history["Open"],ind_history["High"],ind_history["Low"],ind_history["Close"]])#.plot(label='Open')
    fig = go.Figure(data = [go.Candlestick(x = ind_date, open = ind_open, high = ind_high, low = ind_low, close = ind_close)])
    # print(fig.layout.xaxis.range)
    for j in info[2]:
        sma_calc(ind_vals, j)
        w = (2/(j + 1))
        for i in range(0, len(ind_open)):
            try:
                calc = ema_calc(i, ind_vals, w)

            except Exception as e:
                print("Caught in for loop ", e)
        total_ema.append(ema)
        x = r.randint(0, 200)
        y = r.randint(0, 200)
        z = r.randint(0, 200)
        fig.add_trace(go.Scatter(x = ind_date, y = ema, name = str(j) + " EMA",line = dict(color = 'rgb' + str((x, y, z)))))
        ema = [] 

    for i in range (0, len(total_ema[0])):
        macd.append(total_ema[0][i] - total_ema[1][i])

    fig2 = go.Figure(data = [go.Scatter(x = ind_date, y = macd, name = "MACD", line = dict(color = 'purple'))])

    fig.show()  
    fig2.show() 
# run(("NIFTY FUT", "Close", [12, 26, 9], "2021-01-01", "2021-12-31"))
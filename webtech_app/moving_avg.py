import webtech_app.futures as ft
# import futures as ft
import pandas as pd
from datetime import datetime
import plotly.express as px 
import plotly.graph_objects as go
import random as r

global sma
sma = []
def sma_calc(i, ind_vals, days):
    i = i + days - 1
    adder = 0
    for j in range(i, i - days, -1):
        adder = adder + ind_vals[j]

    sma.append(adder/days)


def set_up():
    global sma
    sma = []
   
def run(info):
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

    for j in info[2]:
        set_up()
        for i in range(0, len(ind_open)):
            try:
                sma_calc(i, ind_vals, j)
    
            except Exception as e:
                print("Caught in for loop ", e)

        x = r.randint(0, 200)
        y = r.randint(0, 200)
        z = r.randint(0, 200)
        fig.add_trace(go.Scatter(x = ind_date, y = sma, name = str(j) + " SMA",line = dict(color = 'rgb' + str((x, y, z)))))
    # print(trades )
    fig.show()
    
# run(("NIFTY FUT", "Close", [20, 30, 50], "2021-01-01", "2021-12-31"))
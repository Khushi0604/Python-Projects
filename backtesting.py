import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
)

data['SMA20']=data['AAPL.Close'].rolling(20).mean()
data['SMA50']=data['AAPL.Close'].rolling(50).mean()

data['SIGNAL']=0
data.loc[data['SMA20']>data['SMA50'],'Signal']=1

data['Returns']=data['AAPL.Close'].pct_change()
data['Strategy_Returns']=data['Returns']*data['Signal'].shift(1)

data['Cumulative_Returns']=(1+data['Strategy_Returns']).cumprod()

plt.figure()
plt.plot(data['Cumulative_Returns'])
plt.title("Backtested Strategy Returns")
plt.show()

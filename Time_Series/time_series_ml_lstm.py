import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input 
import matplotlib
matplotlib.use("Agg")

#Time series generation
t=np.arange(0,100,0.1)
series=np.sin(t)

#Data prep
X,y=[],[]

for i in range(len(series)-10):
    X.append(series[i:i+10])
    y.append(series[i+10])

X=np.array(X)
y=np.array(y)

X=X.reshape((X.shape[0],X.shape[1],1))

model=Sequential([
    Input(shape=(10,1)),
    LSTM(32), 
    Dense(1)
])

model.compile(optimizer='adam',loss='mse')
model.fit(X,y,epochs=5,verbose=0)

pred=model.predict(X)

plt.figure()
plt.plot(y,label="Actual")
plt.plot(pred,label='Predicted')
plt.legend()
plt.title("LSTM Time Series Prediction")
plt.savefig("lstm_prediction.png")
plt.close()
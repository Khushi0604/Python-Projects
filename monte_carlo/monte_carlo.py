import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

S0=100
mu=0.0005
sigma=0.01
days=252
simulations=500

prices=np.zeros((days,simulations))
prices[0]=S0

for t in range(1,days):
    prices[t]=prices[t-1]*np.exp(
        (mu-0.5*sigma**2)+sigma*np.random.randn(simulations)
    )

plt.figure()
plt.plot(prices)
plt.title("Monte Carlo Stock Price Simulation")
plt.savefig("MonteCarlo_Simulation.png")
plt.close()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def loadPrices(fileName):
    data = pd.read_csv(fileName, sep=",", header=None)
    data.columns = ["Date", "Open", "High", "Low", 'Price', 'Volume', 'DateEnd']
    return data


# price@t0 = 100%
def normalizeValues(table, newColumn, existingColumn):
    priceAtT0 = table.iloc[+1][existingColumn]
    table[newColumn] = table.apply(lambda row: (row[existingColumn] / priceAtT0), axis=1)

    return table


btc = loadPrices('../data/BTCUSDT_01-01-2022_29-01-2023.txt')
eth = loadPrices('../data/ETHUSDT_01-01-2022_29-01-2023.txt')

#re-index index USD = index Oil
commonIndex = btc.index

#normalizing values
eth = normalizeValues(eth, 'normalizedValue', 'Price')
btc = normalizeValues(btc, 'normalizedValue', 'Price')


Xaxis = commonIndex
# #Y = price
btcYaxis = btc['normalizedValue'].values
ethYAxis = eth['normalizedValue'].values

#
#
#
plt.plot(Xaxis, btcYaxis, color="red", label='BTC')
plt.plot(Xaxis, ethYAxis, 'b--', label='ETH')
plt.legend()
plt.show()

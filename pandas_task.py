import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def create_donut(radius, size=1000):
    # assume that arr is in polar coordinates
    arr = np.repeat(np.linspace(-radius, radius, num=round(size*0.5)), 2)
    print(arr)
    x = np.cos(arr)*radius+np.random.random(size)*3
    y = np.sin(arr)*radius+np.random.random(size)*3
    cartesian_arr = np.array([x, y]).T
    return cartesian_arr



innerCircle = create_donut(5)
outerCircle = create_donut(10)

dataframe1 = pd.DataFrame(innerCircle, columns=['x1', 'x2'])
dataframe1['y'] = 0
dataframe2 = pd.DataFrame(outerCircle, columns=['x1', 'x2'])
dataframe2['y'] = 1

dataframe = pd.concat((dataframe1, dataframe2))

dataframe['x1^2'] = np.square(dataframe['x1'])
dataframe['x2^2'] = np.square(dataframe['x2'])
dataframe['x1*x2'] = dataframe['x1'] * dataframe['x2']
dataframe['dim'] = pd.Series(np.where(dataframe['x1*x2'] > 0, 1, -1))
dataframe['x1^2_show'] = dataframe['x1^2'] * dataframe['dim']
dataframe['x2^2_show'] = dataframe['x2^2'] * dataframe['dim']
print(dataframe)
plt.scatter(dataframe['x1'], dataframe['x2'], c=dataframe['y'])
# plt.scatter(dataframe['x1^2_show'], dataframe['x2^2_show'], c=y2)
plt.savefig('donut.png')

dataframe.to_csv('donut.csv', index=False, header=False)

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

x = np.random.random((100, 2)) * 2 + 2
dataframe = pd.DataFrame(x, columns=['x1', 'x2'])

dataframe['x1^2'] = np.square(dataframe['x1'])
dataframe['x2^2'] = np.square(dataframe['x2'])
dataframe['x1*x2'] = dataframe['x1'] * dataframe['x2']
print(dataframe)
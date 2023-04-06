import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from scipy.stats import norm
from matplotlib.colors import LinearSegmentedColormap
from scipy.signal import convolve2d

hx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
hy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

im = Image.open('lena.png')

# gray = LinearSegmentedColormap('gray', np.mean(im, axis=2))
Gx = convolve2d(np.mean(im, axis=2), hx)
Gy = convolve2d(np.mean(im, axis=2), hy)
G = np.sqrt(np.square(Gx) + np.square(Gy))
plt.imshow(np.mean(im, axis=2), cmap='gray')
plt.show()
plt.imshow(G, cmap='gray')
plt.show()
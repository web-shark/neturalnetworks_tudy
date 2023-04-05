import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from numpy.dual import norm

hx = np.array([[1, 0, -1], [2, 0, -2], [3, 0, -3]])
hy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -3]])

im = Image.open('img_test.jpg')
gray = np.mean(im, axis=2)
x = np.linspace(-6, 6, 100)
fx = norm.pdf(x, loc=0, scale=1)
filt = np.outer(fx, fx)
plt.imshow(filt, cmap=gray)

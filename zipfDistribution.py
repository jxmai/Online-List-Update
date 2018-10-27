import matplotlib.pyplot as plt
from scipy import special
import numpy as np



# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.zipf.html


a = 2. # parameter
s = np.random.zipf(a, 1000)

count, bins, ignored = plt.hist(s[s<50], 50, normed=True)
x = np.arange(1., 50.)
y = x**(-a) / special.zetac(a)
plt.plot(x, y/max(y), linewidth=2, color='r')
plt.show()
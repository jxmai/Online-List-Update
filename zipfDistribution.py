import matplotlib.pyplot as plt
from scipy import special
import numpy as np
from collections import Counter



# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.zipf.html


cnt = Counter()

a = 2 # parameter
s = np.random.zipf(a, 9000)
for i in s:
    cnt[i] += 1
print(cnt)

# count, bins, ignored = plt.hist(s[s<50], 50, normed=True)
# x = np.arange(1., 50.)
# y = x**(-a) / special.zetac(a)
# plt.plot(x, y/max(y), linewidth=2, color='r')
# plt.show()
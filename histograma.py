
# Histograma
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import math
myarr = np.random.randint(low = 0, high = 37, size = 100000)
plt.hist(myarr, bins=37, density=True, color = "green", ec="green")

plt.show()
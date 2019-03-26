
# Histograma
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import math
myarr = np.random.randint(low = 1, high = 37, size = 500)
plt.hist(myarr, bins=36, density=True, color = "green", ec="green")

plt.show()
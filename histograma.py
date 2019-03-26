
# Histograma
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import math
myarr = np.random.randint(low = 1, high = 37, size = 1000)
plt.hist(myarr, bins=36, density=True, color = "pink", ec="pink")
plt.ylabel('Cantidad')
plt.xlabel('Valores')
plt.title('Histograma')
plt.show()
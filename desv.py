import numpy as np
import statistics as stats
import matplotlib.pyplot as plt

rand = np.random.randint(low = 0, high = 37, size = 100)

prom = [rand[0], rand[1]]
desv = [stats.stdev(prom)]
for idx, val in enumerate(rand):
	if idx > 1:
		prom.append(val)
		des = stats.stdev(prom)
		desv.append(des)
plt.plot(desv)
plt.show()
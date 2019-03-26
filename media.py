import numpy as np
from numpy import median
import matplotlib.pyplot as plt

rand = np.random.randint(low = 0, high = 37, size = 500)
prom = [rand[0], rand[1]]
media = [median(prom)]
for idx, val in enumerate(rand):
  if idx > 1:
    prom.append(val)
    med = median(prom)
    media.append(med)
plt.plot(media, color = "green")

plt.show()
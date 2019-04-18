import matplotlib.pyplot as plt
import numpy as np

c = np.random.rand(100)
d = c.comsum()
plt.plot(d,'-')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='./data/inflammation-01.csv', delimiter=',')

# Change figsize (swap width and height)
fig = plt.figure(figsize=(3.0, 9.0))

# Change add_subplot (swap first two parameters)
axes1 = fig.add_subplot(3,1,1)
axes2 = fig.add_subplot(3,1,2)
axes3 = fig.add_subplot(3,1,3)

axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0))

#fig.tight_layout()
fig.set_tight_layout(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt



t1 = np.arange(0.0, 5.0, 0.1)


plt.figure(1)
plt.subplot(211) # rows,columns,currentgraphnumber
line, = plt.plot(t1, t1**2, 'bo')

#line.set_markersize(10)

plt.subplot(212) # switch to second row.
plt.plot(t1, np.cos(np.pi*t1), 'r--')
plt.show()
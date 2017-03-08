import matplotlib.pyplot as plt
import numpy as np

# Data to make your bar graph
# y and x must be same length and order (as always)
y_data = [5,10,7]
x_labels = ['A','B','C']

# Make a bar graph
plt.bar(np.arange(len(y_data)), y_data, 0.8) #x,y,width,kwarg

# Labels your bars on the x axis
plt.xticks(np.arange(len(y_data)), x_labels, rotation=45) #x,y,kwarg

plt.show()



import matplotlib.pyplot as plt
import random

xval = []
yval = []
color = []
size = []
for i in range(50):
    x = (random.randrange(100))
    y = (random.randrange(100))
    if y >= 50:
        color.append("red")
    else:
        color.append("green")
    size.append(abs(100- y))
    xval.append(x)
    yval.append(y)


my_plot = plt.scatter(xval,yval)
my_plot.size(20)

#heatmap = my_plot.pcolor(xval,yval)

plt.show()

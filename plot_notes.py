import matplotlib.pyplot as plt
import numpy as np

# Numpy allows us to make mathematical functions when we don't have discrete x, y data
t = np.arange(1, 8, 0.1)


x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 5, 5, 3, 9, 8, 0, 8]

#plt.plot(x, y) # plots the values (x, y) to the graph

# shortcut styling
#plt.plot(x, y, 'gP--')  # look up shortcuts at matplotlib.org

#create a plot object
line, = plt.plot(x, y) # don't forget a comma
line2, = plt.plot(x, [1,1,1,1,1,1,1,1])
line3,line4,line5 = plt.plot(t, t, t, t**2, t, t**3)


line.set_linewidth(5) # pixels
line.set_color('darkgreen') # look up at matplotlib.org
line.set_alpha(0.5) # alpha is opaqueness from 0.0 to 1.0
line.set_linestyle('--')
line.set_marker('8') # look up under plt.plot or set_properties
line.set_markersize(10)

# takes TeX language between $\symbol$
plt.xlabel("X - Value (units)")
plt.ylabel("Y - Value ($\Omega$)")
plt.title("My cool graph", color="blue")

plt.grid() # turns on major tick grid

ax = plt.gca()



plt.text(4, 25, "My Point")

plt.show() # shows the plotted values as a graph
plt.ylim([50,80])
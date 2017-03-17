#1 Import csv, numpy, and matplotlib.plot
#2 Open the chi_life_expectancy.txt file
#3 Use csv.reader(file, delimeter='\t') to read in the file to a list.  Make appropriate lists for plotting. Community name will be the x and 2010 life expectancy on the y.
#4 Plot the life_expectancy_2010_list vs a numpy arange() as a bar graph
#5 Use ax = plt.gca() to grab the axes object as ax. Use ax.set_xticklabels(community_list) to place the labels on the x axis, use the kwarg rotation=60 to tilt the lettering since there are a lot of communities
#6  Set an appropriate plt.ylim([min,max])
#7  Label your axes
#8  Add a title
#9  Add text to indicate the minimum and maximum values
#10 Customize your graph in at least two other ways using documentation from matplotlib.org
#11  Comment your code as always.

# Note:  If you would like to present something different than the above for your graph using this dataset, just let me know your intentions before you start and I will do my best to support you.


import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from operator import itemgetter


#reading data into list
file = open("chi_life_expectancy.txt", 'r')
life = []
reader = csv.reader(file, delimiter='\t')
for line in reader:
    life.append(line)
print(life)

x_graph = []
y_2010 = []
y_2000 = []
y_1990 = []

life.sort(key=itemgetter(8))   #this is sorting by 2010 life expectancy

for i in range(1, len(life)):       #adding different data to different lists
    x_graph.append(life[i][1])
    y_2010.append(float(life[i][8]))
    y_2000.append(float(life[i][5]))
    y_1990.append(float(life[i][2]))
print(y_2010)
print(y_2000)
print(y_1990)
print(x_graph)

plt.figure(tight_layout = True, figsize = [12,5])   #making everything fit


plt.bar(np.arange(len(y_2010)), y_2010, .8, color = 'green')
plt.bar(np.arange(len(y_2000)), y_2000, .8, color = "blue")
plt.bar(np.arange(len(y_1990)), y_1990, .8, color = "red")
plt.xticks(np.arange(len(x_graph)), x_graph, rotation=90, size = 8)



le_2010 = mpatches.Patch(color = 'green', label = '2010 life exectancy')
le_2000 = mpatches.Patch(color = 'blue', label = '2000')
le_1990 = mpatches.Patch(color = 'red', label = '1990')


plt.legend(handles = [le_2010,le_2000,le_1990], shadow = True)

plt.text(16, 84, "minimum life expectancy = 68.8 years")
plt.text(46, 84, "maximum life expectancy = 85.2 years")
plt.ylim([50, 92])   #scaling the graph



plt.ylabel("Life expectancy in years")
plt.xlabel("Neighborhood")
plt.title("Life Expectancy")



plt.show()




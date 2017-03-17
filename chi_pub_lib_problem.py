

# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
# calculate (and make a list of) the total visitors to Chicago libraries each month.  Do not plot every library individually.  Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend
# label axes, title the graph


import csv
from operator import itemgetter
import matplotlib.patches as mpatches

lib_data = []
file = open("chilib_visitors_2016", 'r')

reader = csv.reader(file, delimiter='\t')
for line in reader:
    lib_data.append(line)
print(lib_data)
print(reader)

headers = lib_data[0]   #this makes the heaerds all the stuff in the first categpry, like the months and all that
lib_data = lib_data[1:]  #new lib data doesnt include the first part with all the months
print(lib_data)

'''
jan = []
feb = []
mar = []
apr = []
may = []
jun = []
july = []
aug = []
sep = []
oct = []
nov = []
dec = []


x = [jan, feb, mar, apr, may, jun, july, aug, sep, oct, nov, dec]



for i in range(0, len(lib_data)):
    x[0].append(lib_data[i][1])
    feb.append(lib_data[i][2])
    mar.append(lib_data[i][3])
    apr.append(lib_data[i][4])
    may.append(lib_data[i][5])
    jun.append(lib_data[i][6])
    july.append(lib_data[i][7])
    aug.append(lib_data[i][8])
    sep.append(lib_data[i][9])
    oct.append(lib_data[i][10])
    nov.append(lib_data[i][11])
    dec.append(lib_data[i][12])

print(jan)
'''

totals = []     #list of total visitors for each motnh

for month in range(12):
    total = 0
    for i in range(len(lib_data)):
        total += int(lib_data[i][month + 1])        #going through and getting totals for each month
    totals.append(total)
print(totals)


for i in range(len(lib_data)):
    lib_data[i][-1] = int(lib_data[i][-1])

lib_data.sort(key=itemgetter(-1))             #sorting by ytd

graph_list = []
most_visited = lib_data[-3:]  #getting top 3 ytd
print(most_visited)
graph_list.append(most_visited)
graph_list.append(totals)       #adding the top 3 most visited plus the totals to a list
print(graph_list)


import matplotlib.pyplot as plt
import numpy as np

headers = headers[1:13]   # making headers just jan through dec
x_graph = headers
y_graph = (totals)
print(headers)

#plt.plot(np.arange(len(y_graph)), y_graph)

plt.xticks(np.arange(len(y_graph)), x_graph, rotation = 65, size = 5)  #size or fontsize to change the size


#plotting
total, = plt.plot(np.arange(len(y_graph)), graph_list[1], '--')
most, = plt.plot(np.arange(len(y_graph)), graph_list[0][2][1:13], '--')
second, = plt.plot(np.arange(len(y_graph)), graph_list[0][1][1:13], '--')
third, = plt.plot(np.arange(len(y_graph)), graph_list[0][0][1:13], '--')

total.set_color("green")
most.set_color('red')
second.set_color("orange")
third.set_color('blue')


total_patch = mpatches.Patch(color = 'green', label = 'total visitors')
most_patch = mpatches.Patch(color = 'red', label = graph_list[0][2][0])   #taking the name of each library
second_patch = mpatches.Patch(color = 'orange', label = graph_list[0][1][0])
third_patch = mpatches.Patch(color = 'blue', label = graph_list[0][0][0])

plt.legend(handles = [total_patch, most_patch,second_patch,third_patch], shadow = True)

plt.ylabel("Number of visitors")
plt.xlabel("Month")
plt.title("Library Visitors")


plt.show()


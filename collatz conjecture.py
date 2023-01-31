import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

k = float(input('input a number\t'))

data = [k]

# make data

def getData(k):
    if k==1:
        return
    elif k%2 == 0:
        k = k/2
        data.append(k)
        getData(k)
    elif k%2 != 0:
        k = (k*3)+1
        data.append(k)
        getData(k)

getData(k)

length = len(data)

x = range(length)
y = data

# plot

plt.plot(x, y,linestyle='-', marker='o')

plt.xticks(x,data)
plt.yticks(data,range(1,length+1))

plt.show()
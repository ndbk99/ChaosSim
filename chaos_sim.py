import matplotlib.pyplot as plt
import numpy as np

# function used to apply to itself
def func(x, r):
    return r * x * (1-x)

"""
algorithm that runs func(x,r) over and over on itself
parameters: tuning parameter r, initial pop %, whether to print info (optional, default False)
return: number of equilibria of that equation
"""
def recursion(r, x, info=False):

    y_values = []

    # iterate function on itself
    for i in range(100):  # range=100,000
        x = func(x, r)  # set new x value to current y value
        y_values.append(x)

    eqs = y_values #find_eqs(y_values)

    # print and plot equilibria info
    if info:
        print(eqs)
        print(len(eqs))
        plt.plot(y_values)
        plt.show()

    return eqs


"""
search for equilibria in function values
parameters: array of function values, boolean of whether to print info (optional, default False)
return: array of equilibria in function values
"""

def find_eqs(arr, info=False):

    # dict holding [possible equilibrium value : number of occurrences]
    values = {}

    # add new equilibria instances to list
    for i in range(1,len(arr)-1):
        rounded = round(arr[i], 4)  # round to 2 decimal places
        minimum = rounded < arr[i-1] and rounded < arr[i+1]  # check if local min
        maximum = rounded > arr[i-1] and rounded > arr[i+1]  # check if local max
        if rounded not in values:
            values[rounded] = 1
        else:
            values[rounded] += 1
        i += 1

    # array holding recurring equilibrium values (n >= 10)
    eqs = []

    # check to see which show up
    for x in values:
        if info:
            print(x)
        if values[x] >= 10:
            eqs.append(x)

    return eqs
    

# generate graph of equilibrium values vs values of r
def plot(pop):
    r_arr = [n * 0.01 for n in range(-1000,1000,1)]

    x = r_arr
    y = []
    for r in r_arr:
        value = recursion(r,pop)
        y.append(tuple(value))

    print(y)

    for xe, ye in zip(x, y):
        plt.scatter([xe] * len(ye), ye, s=0.5)
        print(xe)
    plt.show()
    print("end")


plot(0.5)
# recursion(3.544, 0.5, True)

import matplotlib.pyplot as plt

# function used to apply to itself
def func(x, r):
    return r * (x - x * x)

# single algorithm run
# parameters: tuning parameter r, initial pop %, whether to print info (optional, default False)
# return: number of equilibria of that equation
def recursion(r, x, info=False):
    
    y_values = []

    # iterate function on itself
    for i in range(10000):  # range=100,000
        x = func(x, r)  # set new x value to current y value
        y_values.append(x)

    eqs = find_eqs(y_values)

    # print and plot equilibria info
    if info:
        print(eqs)
        print(len(eqs))
        plt.plot(y_values)
        plt.show()

    return eqs

# search for equilibria in function values
# parameters: array of function values, boolean of whether to print info (optional, default False)
# return: array of equilibria in function values
def find_eqs(arr, info=False):
    
    # dict holding [possible equilibrium value : number of occurrences]
    values = {}
    
    # add new equilibria instances to list
    for i in range(1,len(arr)-1):
        rounded = round(arr[i], 4)  # round to 2 decimal places
        minimum = rounded < arr[i-1] and rounded < arr[i+1]  # check if local min
        maximum = rounded > arr[i-1] and rounded > arr[i+1]  # check if local max
        if minimum or maximum:  # only add to equilibrium values if local min or max
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
    
# PROGRAM MAIN
# parameter: pop - 0 to 1, percent of total possible population at start
# return: y - array of #s of eqs for different values of r
def main(pop):

    # values of r to iterate over
    r_arr = [round(n * 0.001,3) for n in range(2500,4001,1)]

    # store x and y values to plot
    x = []
    y = []
    
    # run algo for different values of r
    for r in r_arr:
        run = len(recursion(r,pop))
        x.append(r)
        y.append(run)
        print(r, run)

    # plot # of eqs over values of r
    plt.plot(x,y)
    plt.show()

    return y

"""
main(0.5)
recursion(3.844,0.5,True)
recursion(3.86,0.5,True)
"""

# recursion(2.9999999999999999999999, 0.5, True)
# generate graph of equilibrium values vs values of r
def plot(pop):
    r_arr = [round(n * 0.001,3) for n in range(1000,4001,1)]

    x = r_arr
    y = []
    for r in r_arr:
        value = recursion(r,pop)
        # print(value)
        y.append(tuple(value))

    print(y)

    for xe, ye in zip(x, y):
        plt.scatter([xe] * len(ye), ye, s=0.5)
    plt.show()

    return -1

plot(0.5)

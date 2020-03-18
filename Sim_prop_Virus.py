import matplotlib.pyplot as plt
import numpy as np
import math
from random import choices
from collections import Counter

plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)

def poisson(lambd, x):
    ret = np.array([])
    for x in x:
        y = np.power(lambd, x) * np.exp(-lambd) / math.factorial(x)
        ret = np.append(ret, y)
    return ret

def convert(x):
    p = 0
    for x in x:
        p = x
    return p

n = 20
x = np.linspace(1, n, n)
average = 1
y = poisson(average, x)

q = choices(x, y, k=1000000)
# plt.plot(x, y, 'v', color='orangered')
plt.hist(q, bins=n)
# plt.show()

population = int(1e6)
infected = int(1)
non_infected = population - infected

days_counter = int(0)
infection_track = np.array([infected])
days = np.array([days_counter])
period = int(10)

plt.figure('Number of people infected')
for k in range(period):
    newly_infected = 0
    for i in range(infected):
        newly_infected = int(convert(choices(x, y, k=1))) + newly_infected
    # print(newly_infected)
    infected = infected + newly_infected
    # non_infected = population - infected
    infection_track = np.append(infection_track, infected)
    days_counter = days_counter + 1
    days = np.append(days, days_counter)

plt.plot(days, infection_track, 'v')
plt.xlabel('Days', fontsize=18)
plt.ylabel('Number of people infected', fontsize=18)
plt.show()
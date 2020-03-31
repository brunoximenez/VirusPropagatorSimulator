import matplotlib.pyplot as plt
import numpy as np
import math
from random import choices

plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)


def poisson(lambd, x):
    ret = np.array([])
    for x in x:
        y = np.power(lambd, x) * np.exp(-lambd) / math.factorial(x)
        ret = np.append(ret, y)
    return ret


n = 10
x = np.linspace(1, n, n)
average = 0.2
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
daily_infected = np.array([int(1)])
period = int(20)


plt.figure('Number of people infected')
for k in range(period):
    newly_infected = 0
    print (k)
    for i in range(infected):
        u = choices(x, y, k=1)
        w = int(u[0])
        newly_infected = w + newly_infected
    print (k)
    # print(newly_infected)
    infected = infected + newly_infected
    daily_infected = np.append(daily_infected, newly_infected)
    # non_infected = population - infected
    infection_track = np.append(infection_track, infected)
    days_counter = days_counter + 1
    days = np.append(days, days_counter)


figure = plt.subplot(3, 1, 1)
plt.tight_layout(h_pad=1.0)
fontsize = 12
plt.plot(days, infection_track, 'v')
plt.ylabel('People infected', fontsize=fontsize)
plt.xlim((0, period + 1))

plt.subplot(3, 1, 2)
plt.ylabel('Daily new cases', fontsize=fontsize)
plt.plot(days, daily_infected, 'v')
plt.xlabel('Days', fontsize=fontsize)
plt.xlim((0, period + 1))

plt.subplot(3, 1, 3)
plt.plot(infection_track, daily_infected, 'v')
plt.xlabel('People infected', fontsize=fontsize)
plt.ylabel('Daily new cases', fontsize=fontsize)
plt.xlim((0, infected+100))
plt.show()

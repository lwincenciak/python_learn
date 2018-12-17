import numpy as np
import matplotlib.pyplot as plt


def silnia(n):
    if n > 1:
        return n * silnia(n - 1)  # wywolanie rekurencyjne funkcji
    elif n in (0, 1):
        return 1


ts_length = 90
b = 46 / 16  # Barcelona currently

# p_values = [0]  # empty list
goals_list = [0, 1, 2, 3, 4]
colors = ['#0055DD', '#009933', '#FF6622', '#FF1122', '#880000']


def poisson(g):
    p_values = []
    for t in range(ts_length + 1):
        p = (np.exp(-(b / 90) * t) * ((b / 90) * t) ** g) / (silnia(g))
        p_values.append(p)
    return p_values


fig = plt.figure(figsize=(10, 8))
plt.xlim(0, ts_length)
# plt.ylim(3.35, 3.65)

plt.rcParams.update({'font.size': 14})

i = 0
for g in goals_list:
    x = poisson(g)
    plt.plot(x, linewidth=2.5, color=colors[i], label='g = ' + str(g))
    i += 1

plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
plt.xlabel('Time [t]')
plt.ylabel('')
plt.title('Probability of scoring by Barcelona\n given number of goals in a game')
plt.legend()
plt.show()
fig.savefig("poisson.pdf")

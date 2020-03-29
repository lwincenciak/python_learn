import numpy as np
import matplotlib.pyplot as plt


def silnia(n):
    if n > 1:
        return n * silnia(n - 1)  # wywolanie rekurencyjne funkcji
    elif n in (0, 1):
        return 1


match_length = 90
<<<<<<< HEAD
b = 42 / 17  # Liverpool currently
=======
b = 42 / 17  # Barcelona currently
>>>>>>> 48be04d12532ceeeed368d1f1eb70ca383b39bf9

# p_values = [0]  # empty list
goals_list = [0, 1, 2, 3, 4]
colors = ['#0055DD', '#009933', '#FF6622', '#FF1122', '#880000']


def poisson(g):
    p_values = []
    for t in range(match_length + 1):
        p = (np.exp(-(b / 90) * t) * ((b / 90) * t) ** g) / (silnia(g))
        p_values.append(p)
    return p_values


fig = plt.figure(figsize=(12, 8))
plt.xlim(0, match_length)
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
<<<<<<< HEAD
plt.title('Probability of scoring given number of goals\n by Liverpool during a game')
=======
plt.title('Probability of scoring given number of goals\n by Liverpool during a game\n with an average of 2.47 per game')
>>>>>>> 48be04d12532ceeeed368d1f1eb70ca383b39bf9
plt.legend()
plt.show()
fig.savefig("poisson.pdf")

import numpy as np
import matplotlib.pyplot as plt

ts_length = 200
# x_values = [0]  # empty list
r_list = [3, 3.449, 3.569946]
colors = ['#0055DD', '#009933', '#BB0022']


def tseries(r):
    x_values = []
    x = 0.5
    for t in range(ts_length + 1):
        x = r * x * (1 - x)
        x_values.append(x)
    return x_values


fig = plt.figure(figsize=(12, 6))
plt.xlim(0, ts_length)
# plt.ylim(3.35, 3.65)

plt.rcParams.update({'font.size': 14})

i = 0
for r in r_list:
    x = tseries(r)
    plt.plot(x, linewidth=1.2, color=colors[i], label='$\\alpha = $' + str(r))
    i += 1

plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
plt.xlabel('Time [t]')
plt.ylabel('')
plt.title('Time series for different r parameter\n$x_{t+1} = k x_t (1 - x_t)$')
plt.legend()
plt.show()
fig.savefig("chaos.pdf", bbox_inches='tight')

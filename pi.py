import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

iterations = 1000
n = 9999
# definitions


def my_print(text):
    sys.stdout.write(str(text))
    sys.stdout.flush()


def kropki(num):
    my_print(".")
    rest1 = int(num) % 50
    rest2 = int(num) % 10
    if rest2 == 0:
        my_print("|")
    if rest1 == 0:
        print(" : " + str(num))


pi_file = open("pi_mc.csv", "w")
pi = []

for j in range(iterations):
    pi = []  # disable for convergence
    k = 0
    for i in range(n):
        u, v = np.random.uniform(), np.random.uniform()
        d = np.sqrt((u)**2 + (v)**2)
        if d < 1:
            k += 1
    area_estimate = k / n
    p = area_estimate * 4
    pi.append(p)
    pi_av = np.average(pi)
    pi_file.write(str(j + 1) + ";")
    pi_file.write(str(pi_av) + "\n")
    kropki(j + 1)

pi_file.close()

x = []
y = []

with open('pi_mc.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append(int(row[0]))
        y.append(float(row[1]))

plt.rcParams.update({'font.size': 16})

fig = plt.figure(figsize=(18, 8))
plt.xlim(0, iterations)
# plt.ylim(3.35, 3.65)
line1 = plt.plot(x, y, label='Average $\\pi$')
plt.setp(line1, linewidth=0.6, color='#0055FF')
plt.xlabel('Iteration')
plt.ylabel('$\\pi$')
plt.title('Simulation of $\\pi$')
plt.legend()
plt.xticks()
plt.yticks()
plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
plt.show()

fig.savefig("pi_mc.pdf")
fig.savefig("pi_mc.eps", bbox_inches='tight')

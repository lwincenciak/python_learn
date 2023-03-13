import numpy as np
import matplotlib.pyplot as plt


colors = ['#0088EE', '#00DD33', '#FF3322', '#BBAA00']


def collatz(N):
    iteration = 0
    listNumbers = [N]

    while N != 1:
        iteration += 1
        if (N % 2) == 0:
            N = N/2
        else:
            N = (3*N) + 1
        listNumbers.append(N)
    return listNumbers, iteration


fig, ax = plt.subplots(figsize=(11, 6))
i = 0
while i < 4:
    num = int(input('Enter a number: '))
    colnumb, iter = collatz(num)
    print('There are', iter, 'iterations for number', num)
    x = np.arange(0, iter + 1)
    ax.plot(x, colnumb, color=colors[i], lw=2, label='Number: ' + str(num))
    i += 1

plt.title('Collatz Conjecture')
plt.xlabel('Number of iterations')
plt.ylabel('Numbers')
plt.legend(loc="upper right", fontsize=9)
plt.grid()
plt.show()
fig.savefig("collatz.pdf")
fig.savefig("collatz.png")

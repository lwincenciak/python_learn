import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def f(x, t):
    a = 4
    b = 7
    n = x[0]
    c = x[1]
    dndt = a * n - (c / (c + 1)) * b * n
    dcdt = (c / (c + 1)) * n - c + 1
    return [dndt, dcdt]


t = np.linspace(0, 20)
x0 = [20, 5]

x = odeint(f, x0, t)

plt.plot(t, x[:, 0], 'r--', linewidth=2.0)
plt.plot(t, x[:, 1], 'b-', linewidth=2.0)
plt.xlabel("t")
plt.ylabel("S[N, C]")
plt.legend(["N", "C"])
plt.show()

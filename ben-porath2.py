import numpy as np
import matplotlib.pyplot as plt

# definition of parameters
T = 60
a = 0.71
A = 0.75
h0 = 3
r = 0.05
d = 0.06
s0 = 1
theta_list = [0.38, 0.45, 0.5]
colors = ['#0088EE', '#00DD33', '#FF3322']


def benporath(z, a, A, r, d):
    h_values = [h0]
    s_values = []
    w_values = []
    h = h0
    s = s0
    for t in range(T + 1):
        lam = (A * np.exp(-r * t)) * (1 - np.exp(-(r + d) * (T - t))) / (r + d)
        if lam == 0:
            sh = 0
        else:
            sh = ((A * np.exp(-r * t)) / (a * z * lam)) ** (1 / (a - 1))
        s = min(1, (sh / h))
        h = h + z * (h * s) ** a - d * h
        w = A * (1 - s) * h
        s_values.append(s)
        h_values.append(h)
        w_values.append(w)
    return h_values, s_values, w_values


fig = plt.figure(figsize=(12, 12))
plt.xlim(0, T)
# plt.ylim(3.35, 3.65)

plt.rcParams.update({'font.size': 14})

h1, s1, w1 = benporath(0.5, 0.71, 0.75, 0.05, 0.06)
h2, s2, w2 = benporath(0.5, 0.71, 0.75, 0.05, 0.07)
h3, s3, w3 = benporath(0.5, 0.71, 0.75, 0.05, 0.08)

plt.plot(s1, linewidth=2.5, color=colors[0])
plt.plot(s2, linewidth=2.5, color=colors[1])
plt.plot(s3, linewidth=2.5, color=colors[2])

plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
plt.xlabel('Years [t]')
plt.ylabel('s(t)')
plt.legend()
plt.show()
fig.savefig("benporath.pdf")

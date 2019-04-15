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


fig = plt.figure(figsize=(14, 4))
plt.xlim(0, T)
# plt.ylim(3.35, 3.65)

plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'figure.titlesize': 14})

i = 0
for z in [0.38, 0.45, 0.5]:
    h, s, w = benporath(z, 0.71, 0.75, 0.05, 0.06)
    plt.suptitle('Ben-Porath (1967) model of human capital in a life-cycle')
    plt.subplot(1, 3, 1)
    plt.plot(s, linewidth=1.5, color=colors[i], label='$\\theta = $' + str(z))
    plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    plt.title('Schooling effort')
    plt.legend()
    plt.xlabel('Years [t]')
    plt.ylabel('s(t)')
    plt.subplot(1, 3, 2)
    plt.plot(h, linewidth=1.5, color=colors[i], label='$\\theta = $' + str(z))
    plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    plt.title('Human capital')
    plt.legend()
    plt.xlabel('Years [t]')
    plt.ylabel('h(t)')
    plt.subplot(1, 3, 3)
    plt.plot(w, linewidth=1.5, color=colors[i], label='$\\theta = $' + str(z))
    plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    plt.title('Wages')
    plt.legend()
    plt.xlabel('Years [t]')
    plt.ylabel('w(t)')
    i += 1

plt.subplots_adjust(left=0.05, right=0.95, top=0.83, bottom=0.15)
plt.show()
fig.savefig("benporath.pdf")
fig.savefig("benporath.eps")

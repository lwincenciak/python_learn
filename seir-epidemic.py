import pandas as pd
from matplotlib import rc
import numpy as np
import matplotlib.pyplot as plt

# definition of parameters
T = 400
D_incubation = 5.2
D_infectious = 2.9
D_death = 18
D_hospital_lag = 5
D_recovery_severe = 21
a = 1 / D_incubation
gamma = 1 / D_infectious
p_severe = 0.19
p_fatal = 0.02
p_mild = 1 - p_severe - p_fatal
r0 = 2.2
Poland = 38000000

colors = ['#ffe6cc', '#FF3322', '#0088EE', '#001188']
kolory = ['#ff1111', '#11ff11', '#0088EE']


def seir_epi(pop, inter_time, inter_par):
    S_values = []  # susceptible
    E_values = []  # exposed
    Inf_values = []  # infectious
    R_values = []  # removed (no longer exposed or infectious)
    F_values = []  # dead
    D_values = []
    Severe_values = []
    Severe_H_values = []
    S = pop - 1
    E = 0
    Inf = 1
    R = 0
    F = 0
    D = 0
    Severe = 0
    Severe_H = 0
    for t in range(T + 1):
        if t < inter_time:
            beta = r0 / D_infectious
        else:
            beta = (inter_par * r0) / D_infectious

        dS = -beta * (Inf * S) / pop
        dE = (beta * Inf * S) / pop - a * E
        dInf = a * E - gamma * Inf
        dR = gamma * Inf
        dF = p_fatal * gamma * Inf - (1 / D_death) * F
        dD = (1 / D_death) * F
        dSevere = p_severe * gamma * Inf - (1 / D_hospital_lag) * Severe
        dSevere_H = (1 / D_hospital_lag) * Severe - (1 / D_recovery_severe) * Severe_H
        S += dS
        E += dE
        Inf += dInf
        R += dR
        F += dF
        D += dD
        Severe += dSevere
        Severe_H += dSevere_H
        S_values.append(S)
        E_values.append(E)
        Inf_values.append(Inf)
        R_values.append(R)
        F_values.append(F)
        D_values.append(D)
        Severe_values.append(Severe)
        Severe_H_values.append(Severe_H)
    return S_values, E_values, Inf_values, R_values, F_values, D_values, Severe_values, Severe_H_values


# S, E, Inf, R, F, D, Severe, Severe_H = seir_epi(Poland, 80, 0.2)

# for time in range(20):
#    print(str(time) + ': ' + str(D[time]))

fig = plt.figure(figsize=(24, 8))
plt.xlim(0, T)
# plt.ylim(3.35, 3.65)

plt.rcParams.update({'font.size': 12})
plt.rcParams.update({'figure.titlesize': 16})

inter_times = [70, 75, 80]
inter_pars = [0.6, 0.5, 0.44]

i = 0
for z in inter_times:
    S, E, Inf, R, F, D, Severe, Severe_H = seir_epi(Poland, z, 0.42)
    plt.suptitle('SEIR model of epidemic')
    plt.subplot(1, 3, 1)
    plt.plot(Inf, linewidth=1.5, color=kolory[i], label='$t = $' + str(z))
    plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    plt.title('Infectious')
    plt.legend()
    plt.xlabel('Days [t]')
    plt.ylabel('I(t)')
    plt.subplot(1, 3, 2)
    plt.plot(E, linewidth=1.5, color=kolory[i], label='$t = $' + str(z))
    plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    plt.title('Exposed')
    plt.legend()
    plt.xlabel('Days [t]')
    plt.ylabel('E(t)')
    plt.subplot(1, 3, 3)
    plt.plot(D, linewidth=1.5, color=kolory[i], label='$t = $' + str(z))
    plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    plt.title('Deaths')
    plt.legend()
    plt.xlabel('Days [t]')
    plt.ylabel('D(t)')
    i += 1

plt.subplots_adjust(left=0.05, right=0.95, top=0.83, bottom=0.15)
plt.show()
fig.savefig("seir_epid.pdf")

'''
ind = np.arange(T)
barWidth = 0.4
plt.bar(ind, E, color='#7f6d5f', edgecolor='white', width=barWidth)
plt.show()

ind = np.arange(T)
width = 0.4

# Values of each group
bars1 = np.array(D)
bars2 = np.array(Severe_H)
bars3 = np.array(Inf)
bars4 = np.array(E)

# Heights of bars1 + bars2
# bars12 = np.add(bars1, bars2)
# bars123 = np.add(bars1, bars2, bars3)

# The position of the bars on the x-axis
ind = np.arange(T)
barWidth = 0.4

plt.bar(ind, np.add(np.add(bars1, bars2), bars3), color='yellow', edgecolor='yellow')
plt.bar(ind, np.add(bars1, bars2), color='purple', edgecolor='purple')
plt.bar(ind, bars1, color='green', edgecolor='green')
plt.show()
'''

from matplotlib import rc
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


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

# beta = r0 / D_infectious
pop = Poland


def f(x, t, t_inter, t_parm):
    S = x[0]
    E = x[1]
    Inf = x[2]
    R = x[3]
    F = x[4]
    D = x[5]
    Severe = x[6]
    Severe_H = x[7]
    if t < t_inter:
        beta = r0 / D_infectious
    else:
        beta = (t_parm * r0) / D_infectious
    dSdt = -beta * (Inf * S) / pop
    dEdt = (beta * Inf * S) / pop - a * E
    dInfdt = a * E - gamma * Inf
    dRdt = gamma * Inf
    dFdt = p_fatal * gamma * Inf - (1 / D_death) * F
    dDdt = (1 / D_death) * F
    dSeveredt = p_severe * gamma * Inf - (1 / D_hospital_lag) * Severe
    dSevere_Hdt = (1 / D_hospital_lag) * Severe - (1 / D_recovery_severe) * Severe_H
    return [dSdt, dEdt, dInfdt, dRdt, dFdt, dDdt, dSeveredt, dSevere_Hdt]


t = np.arange(0, T, 0.1)
x0 = [pop - 1, 0, 1, 0, 0, 0, 0, 0]

int_time_list = [80, 85, 90]
k = 0.4
int_parm_list = [0.6, 0.8, 1]
ti = 85
kolory = ['#0088EE', '#11ff11', '#ff1111']

i = 0
for z in int_time_list:
    x = odeint(f, x0, t, args=(z, k))

    # Rysujemy wyniki
    plt.rcParams.update({'font.size': 18})
    plt.rcParams.update({'figure.titlesize': 22})

    fig = plt.figure(1, figsize=(24, 15))
    # plt.suptitle('SEIR model of epidemic')
    # Liczba zarazonych
    ax1 = fig.add_subplot(311)
    ax1.plot(t, x[:, 2], color=kolory[i], linewidth=4.0,
             label='$T_{int} = $' + str(z) + ', $\\alpha = $' + str(k))
    ax1.set_xlabel('time')
    ax1.set_ylabel('Infectious')
    ax1.set_xlim(0, T)
    ax1.legend()
    ax1.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    ax1.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # Liczba hispitalizowanych
    ax2 = fig.add_subplot(312)
    ax2.plot(t, x[:, 7], color=kolory[i], linewidth=4.0,
             label='$T_{int} = $' + str(z) + ', $\\alpha = $' + str(k))
    ax2.set_xlabel('time')
    ax2.set_ylabel('Hospitalized')
    ax2.set_xlim(0, T)
    ax2.legend()
    ax2.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    ax2.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # Liczba zmarlych
    ax3 = fig.add_subplot(313)
    ax3.plot(t, x[:, 5], color=kolory[i], linewidth=4.0,
             label='$T_{int} = $' + str(z) + ', $\\alpha = $' + str(k))
    ax3.set_xlabel('time')
    ax3.set_ylabel('Deaths')
    ax3.set_xlim(0, T)
    ax3.legend()
    ax3.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    ax3.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    i += 1

# plt.tight_layout()
plt.show()
fig.savefig("seir_ode_epid.pdf")
fig.savefig("seir_ode_epid.eps")

j = 0
for z in int_parm_list:
    v = odeint(f, x0, t, args=(ti, z))

    # Rysujemy wyniki
    plt.rcParams.update({'font.size': 18})
    plt.rcParams.update({'figure.titlesize': 22})

    fig = plt.figure(1, figsize=(24, 15))
    # plt.suptitle('SEIR model of epidemic')
    # Liczba zarazonych
    ax1 = fig.add_subplot(311)
    ax1.plot(t, v[:, 2], color=kolory[j], linewidth=4.0,
             label='$T_{int} = $' + str(ti) + ', $\\alpha = $' + str(z))
    ax1.set_xlabel('time')
    ax1.set_ylabel('Infectious')
    ax1.set_xlim(0, T)
    ax1.legend()
    ax1.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    ax1.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # Liczba hispitalizowanych
    ax2 = fig.add_subplot(312)
    ax2.plot(t, v[:, 7], color=kolory[j], linewidth=4.0,
             label='$T_{int} = $' + str(ti) + ', $\\alpha = $' + str(z))
    ax2.set_xlabel('time')
    ax2.set_ylabel('Hospitalized')
    ax2.set_xlim(0, T)
    ax2.legend()
    ax2.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    ax2.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    # Liczba zmarlych
    ax3 = fig.add_subplot(313)
    ax3.plot(t, v[:, 5], color=kolory[j], linewidth=4.0,
             label='$T_{int} = $' + str(ti) + ', $\\alpha = $' + str(z))
    ax3.set_xlabel('time')
    ax3.set_ylabel('Deaths')
    ax3.set_xlim(0, T)
    ax3.legend()
    ax3.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
    ax3.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    j += 1

# plt.tight_layout()
plt.show()
fig.savefig("seir_ode_epid2.pdf")
fig.savefig("seir_ode_epid2.eps")

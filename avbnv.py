Poland = 38000000
T = 10
S_values = []  # susceptible
E_values = []  # exposed


def seir_epi(pop):
    S = 1
    E = 1
    S_values.append(S)
    E_values.append(E)
    for t in range(T + 1):
        dS = S
        dE = 2 * E
        S += dS
        E += dE
        S_values.append(S)
        E_values.append(E)
    return S_values, E_values


S, E = seir_epi(Poland)

for time in range(T + 1):
    print(str(time) + ': ' + str(S[time]) + '   ' + str(E[time]))

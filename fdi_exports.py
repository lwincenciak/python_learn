import matplotlib.pyplot as plt

# definition of parameters of the model
B = 1
epsilon = 3
A = B * (epsilon ** epsilon) / (epsilon - 1) ** (epsilon - 1)
fpl = 3
fx = 5
t = 1.15
colors = ['#0088EE', '#00DD33', '#FF3322', '#bbaa00']

# critical fi
fi_dom = (fpl / B) ** (1 / (epsilon - 1))
fi_exp = (fx / (B * (t ** (1 - epsilon)))) ** (1 / (epsilon - 1))
fi_fdi = ((fpl + fx) / B) ** (1 / (epsilon - 1))
fi_exp_fdi = (fpl / (B * (1 - t ** (1 - epsilon)))) ** (1 / (epsilon - 1))

# fi range
Fi = round(fi_exp_fdi + 1.1)

'''
# Function for calculating profits and storing them in arrays
def profits(B, epsilon, fpl, fx, t):
    y_dom_values = []
    y_exp_values = []
    y_fdi_values = []
    y_total_values = []
    x_values = []
    for i in range(1, 201):
        z = (i / 200) * Fi
        x_values.append(z)
        y_dom = B * (z ** (epsilon - 1)) - fpl
        y_exp = B * (t ** (1 - epsilon)) * (z ** (epsilon - 1)) - fx
        y_fdi = B * (z ** (epsilon - 1)) - fpl - fx
        y_total = max(y_dom, y_dom + max(y_fdi, y_exp), 0)
        y_dom_values.append(y_dom)
        y_exp_values.append(y_exp)
        y_fdi_values.append(y_fdi)
        y_total_values.append(y_total)
    return y_dom_values, y_exp_values, y_fdi_values, y_total_values, x_values


y_dom1, y_exp1, y_fdi1, pi_total1, x = profits(B, epsilon, fpl, fx, t)
'''


# Alternative function for calculating profits and storing them in arrays
def profit(A, epsilon, fpl, fx, t):
    pi_dom_values = []
    pi_exp_values = []
    pi_fdi_values = []
    pi_total_values = []
    x_values = []
    for i in range(1, 201):
        z = (i / 200) * Fi
        x_values.append(z)
        p = (epsilon / (epsilon - 1)) * (1 / z)
        px = (epsilon / (epsilon - 1)) * (t / z)
        q = A * (p ** -epsilon)
        qx = A * (px ** -epsilon)
        pi_dom = p * q - fpl - (q / z)
        pi_exp = px * qx - fx - (qx * t) / z
        pi_fdi = p * q - fpl - fx - (q / z)
        pi_total = max(pi_dom, pi_dom + max(pi_fdi, pi_exp), 0)
        pi_dom_values.append(pi_dom)
        pi_exp_values.append(pi_exp)
        pi_fdi_values.append(pi_fdi)
        pi_total_values.append(pi_total)
    return pi_dom_values, pi_exp_values, pi_fdi_values, pi_total_values, x_values


pi_dom1, pi_exp1, pi_fdi1, pi_total1, x = profit(A, epsilon, fpl, fx, t)

font = {'family': 'arial',
        'color': 'black',
        'weight': 'normal',
        'size': 9,
        }

plt.rcParams.update({'font.size': 10})

# Plot profit lines
fig, ax = plt.subplots(figsize=(11, 6))
ax.plot(x, pi_dom1, linewidth=2, color=colors[0], label="Domestic")
ax.plot(x, pi_exp1, linewidth=2, color=colors[1], label="Exports")
ax.plot(x, pi_fdi1, linewidth=2, color=colors[2], label="FDI")
ax.plot(x, pi_total1, linewidth=2, color=colors[3], label="Total")

# dotted lines
X1 = [fi_dom, fi_dom]
Y1 = [min(pi_fdi1), max(pi_total1)]
X2 = [fi_exp, fi_exp]
Y2 = [min(pi_fdi1), max(pi_total1)]
X3 = [fi_exp_fdi, fi_exp_fdi]
Y3 = [min(pi_fdi1), max(pi_total1)]

# Plot dotted lines
plt.plot(X1, Y1, linestyle='--', color='black', lw=.5)
plt.plot(X2, Y2, linestyle='--', color='black', lw=.5)
plt.plot(X3, Y3, linestyle='--', color='black', lw=.5)

# texts
ax.text(fi_dom / 2, max(pi_total1) * 0.96, "EXIT", fontdict=font, horizontalalignment='center',
        verticalalignment='center',)
ax.text(fi_dom + (fi_exp - fi_dom) / 2, max(pi_total1) * 0.96, "DOMESTIC", fontdict=font, horizontalalignment='center',
        verticalalignment='center',)
ax.text(fi_exp + (fi_exp_fdi - fi_exp) / 2, max(pi_total1) * 0.96, "EXPORTS", fontdict=font,
        horizontalalignment='center', verticalalignment='center',)
ax.text(fi_exp_fdi + (Fi - fi_exp_fdi) / 2, max(pi_total1) * 0.96, "FDI", fontdict=font, horizontalalignment='center',
        verticalalignment='center',)

# plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
plt.ylabel('Profit')
ax.set_xlabel('Productivity, $\\varphi$')
ax.xaxis.set_label_coords(.9, .1)
# plt.suptitle('Productivity and firm organization')

ax.set_title('Productivity and firm organization', fontsize=18, color='black', fontweight='normal', loc='center',
             pad=10)

plt.axhline(color='black', lw=0.5)
plt.axvline(color='black', lw=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# set the x-spine
ax.spines['left'].set_position('zero')  # type: ignore

# set the y-spine
ax.spines['bottom'].set_position('zero')  # type: ignore

xticks = ax.xaxis.get_major_ticks()
yticks = ax.yaxis.get_major_ticks()
xticks[1].set_visible(False)
yticks[2].set_visible(False)

plt.legend(bbox_to_anchor=(0.05, 0.5), loc="center left", fontsize=8)
plt.show()
fig.savefig("fdi_exports.pdf")

# This is a simple simulation of throwing a dice a number of times
# The average and std. dev. are calculated and stored in a list
# Everything is then exported to a file 'dice_mc.csv'
import numpy as np
import sys
import random
import matplotlib.pyplot as plt
import csv
# from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter


def roll_dice(number):
    return random.randint(1, number)


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


def minor_tick(x, pos):
    if not x % 1.0:
        return ""
    return "%.2f" % x


dice_throws = 4800
iterations = 1000

dice_file = open("dice_mc.csv", "w")
# dice_file.write("Average;Std\n")
dice_file = open("dice_mc.csv", "a")

for z in range(iterations):
    dice = []  # this clears the list of dice results for every z!
    for i in range(dice_throws):
        # print("Rolling dice " + str(i))
        # print(ut.roll_dice(6))
        dice.append(roll_dice(6))
        # print(dice)
    dice_av = np.average(dice)
    dice_std = np.std(dice)
    # print("Average: " + str(dice_av))
    # print("Stdev. : " + str(dice_std))
    dice_file.write(str(z + 1) + ";")
    dice_file.write(str(dice_av) + ";")
    dice_file.write(str(dice_std) + "\n")
    kropki(z + 1)

dice_file.close()
print("\nOutput written to file: dice_mc.csv")

# printing contents of the file dice_mc.txt
# print("\n")
# dice_file = open("dice_mc.txt", "r")
# print(dice_file.read())
# dice_file.close()


# I would like to draw the results by reading the FileExistsError

x = []
y = []

with open('dice_mc.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append(int(row[0]))
        y.append(float(row[1]))

plt.rcParams.update({'font.size': 12})

fig = plt.figure(figsize=(12, 8))
plt.xlim(0, iterations)
# plt.ylim(3.40, 3.60)
line1 = plt.plot(x, y, label='Average score')
plt.setp(line1, linewidth=0.6, color='#0055FF')
plt.xlabel('Iteration')
plt.ylabel('Average score')
plt.title('Simulation of ' + str(dice_throws) +
          ' throws of a dice\nRepeated ' + str(iterations) + ' times')
plt.legend()
plt.xticks()
plt.yticks()
plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
plt.show()

fig.savefig("dice_mc.pdf", bbox_inches='tight')
fig.savefig("dice_mc.eps", bbox_inches='tight')

# This is a simple simulation of throwing a dice a number of times
# The average and std. dev. are calculated and stored in a list
# Everything is then exported to a file 'dice_mc.csv'
import useful_tools as ut
import numpy as np
import sys


def my_print(text):
    sys.stdout.write(str(text))
    sys.stdout.flush()


def kropki(num):
    my_print(".")
    rest = int(num) % 50
    if rest == 0:
        print(" " + str(num))


dice_throws = 1200
iterations = 200

dice = []
dice_file = open("dice_mc.csv", "w")
dice_file.write("Average;Std\n")
dice_file = open("dice_mc.csv", "a")

for z in range(iterations):
    for i in range(dice_throws):
        # print("Rolling dice " + str(i))
        # print(ut.roll_dice(6))
        dice.append(ut.roll_dice(6))
        # print(dice)
    dice_av = np.average(dice)
    dice_std = np.std(dice)
    # print("Average: " + str(dice_av))
    # print("Stdev. : " + str(dice_std))
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

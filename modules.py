# importing external modules - like external code
# list of Python modules docs.python.org/3/py-modindex.html
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


dice_throws = 1000
iterations = 300

dice = []
dice_file = open("dice_mc.txt", "w")
dice_file.write("Average;Std\n")
dice_file = open("dice_mc.txt", "a")

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
print("\nOutput written to file: dice_mc.txt")
# print("\n")
# dice_file = open("dice_mc.txt", "r")
# print(dice_file.read())
# dice_file.close()

# print(ut.queen)

'''
wzrost = [1.72, 1.75, 1.83, 1.95, 1.77]
waga = [67.6, 71.3, 72.8, 83.1, 73.9]

np_wzrost = np.array(wzrost)
np_waga = np.array(waga)

bmi = np_waga / np_wzrost ** 2
bmi_av = np.average(bmi)
bmi_std = np.std(bmi)

print(bmi)
print(bmi_av)
print(bmi_std)
'''

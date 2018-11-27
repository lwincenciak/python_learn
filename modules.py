# importing external modules - like external code
# list of Python modules docs.python.org/3/py-modindex.html
import useful_tools as ut
import numpy as np

for i in range(12):
    print(ut.roll_dice(6))

print(ut.queen)

wzrost = [1.72, 1.75, 1.83, 1.95, 1.68]
waga = [67.6, 75.3, 72.8, 86.1, 79.9]

np_wzrost = np.array(wzrost)
np_waga = np.array(waga)

bmi = np_waga / np_wzrost ** 2

print(bmi)

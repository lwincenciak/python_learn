# importing external modules - like external code
# list of Python modules docs.python.org/3/py-modindex.html
import useful_tools as ut
import numpy as np

print(ut.queen)

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

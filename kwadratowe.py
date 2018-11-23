from math import *

a = input("a = ")
b = input("b = ")
c = input("c = ")
delta = float(b) * float(b) - 4 * float(a) * float(c)
print("\nRownanie kwadratowe: " + a + "x^2 + " + b + "x + " + c + " = 0")
print("Delta =" + str(delta))

if delta < 0:
    print('Rownanie nie ma pierwiastkow.')
else:
    if delta == 0:
        print('Rownanie ma jeden pierwiastek.')
        x = -float(b) / (2 * float(a))
        print('x1 = x2 = ' + str(x))
    else:
        delt = sqrt(float(delta))
        print('Rownanie ma dwa pierwiastki')
        x_1 = (-float(b) - float(delt)) / (2 * float(a))
        x_2 = (-float(b) + float(delt)) / (2 * float(a))
        print('x1 = ' + str(x_1))
        print('x2 = ' + str(x_2))

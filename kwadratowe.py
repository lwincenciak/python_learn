from math import *

a = input("a = ")
b = input("b = ")
c = input("c = ")

if float(b) >= 0:
    znak_b = "+"
else:
    znak_b = ""

if float(c) >= 0:
    znak_c = "+"
else:
    znak_c = ""

delta = float(b) * float(b) - 4 * float(a) * float(c)
print("\nRownanie kwadratowe: " + a + "x² " + znak_b + b + "x " + znak_c + c + " = 0")
print("Δ = " + str(delta))

if delta < 0:
    print('Rownanie nie ma pierwiastkow rzeczywistych.')
else:
    if delta == 0:
        print('Rownanie ma jeden pierwiastek rzeczywisty:')
        x = -float(b) / (2 * float(a))
        print('x₁ = x₂ = ' + str(x))
    else:
        delt = sqrt(float(delta))
        print('Rownanie ma dwa pierwiastki rzeczywiste:')
        x_1 = (-float(b) - float(delt)) / (2 * float(a))
        x_2 = (-float(b) + float(delt)) / (2 * float(a))
        print('x₁ = ' + str(x_1))
        print('x₂ = ' + str(x_2))

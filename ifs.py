import os

is_male = False
is_tall = False
name = input('Twoje imie: ')
height = input('Twoj wzrost w cm: ')
while not(height.isdigit()):
    print('Niepoprawna wartosc, podaj jeszcze raz')
    height = input('Twoj wzrost w cm: ')

os.system('cls')

if name[-1] == 'a':
    is_male = False
else:
    is_male = True

if is_male and float(height) > 175:
    is_tall = True
elif not(is_male) and float(height) > 165:
    is_tall = True
else:
    is_tall = False

'''
if is_male or is_tall:
    print('You are male or tall')
else:
    print('You are not a male or not tall or both')
'''

if is_male and is_tall:
    print('Jestes wysokim mezczyzna')
elif is_male and not(is_tall):
    print('Jestes niskim mezczyzna')
elif not(is_male) and (is_tall):
    print('Jestes wysoka kobieta')
else:
    print('Jestes niska kobieta')

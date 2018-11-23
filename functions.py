def say_hi():
    print('-------------------')
    print('--- Hello user! ---')
    print('-------------------')


say_hi()


def say_hello(name):
    print('-------------------')
    print('Hello ' + name + '!')
    print('-------------------')


imie = input('What\'s your name? ')
say_hello(imie)


def witaj(name, sex):
    print('-------------------')
    print('Hello ' + name + '!')
    print('You are a great ' + sex + '!')
    print('-------------------')


imie = input('What is your name? ')
pl = input('What is your sex? ')

witaj(imie, pl)

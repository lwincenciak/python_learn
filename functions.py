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


imie = input('What\'s your name? ')
plec = input('What\'s your sex? ')

witaj(imie, plec)

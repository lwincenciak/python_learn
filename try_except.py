# Try the block of code
# if there is no error go ahead
# if there is, then do something else (except)
# we can specify the specific types of errors, not just everything


try:
    value = 10 / 60
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)

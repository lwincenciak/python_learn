# example of a loop
print(2**10)


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 2))
print(raise_to_power(3, 4))
print(raise_to_power(2, 20))

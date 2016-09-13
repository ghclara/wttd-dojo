def sum_of_squares(number):
    return sum([int(char) ** 2 for char in str(number)])


def happy(number):
    box = []
    n = number
    while n != 1 and n not in box:
        box.append(n)
        n = sum_of_squares(n)
    return n == 1


def recursive_happy(number):
    if number < 10:
        return number in (1, 7)
    _next = sum_of_squares(number)
    return happy(_next)


assert happy(1)
assert not happy(4)
assert happy(10)
assert happy(100)
assert happy(130)
assert happy(97)


assert recursive_happy(1)
assert not recursive_happy(4)
assert recursive_happy(10)
assert recursive_happy(100)
assert recursive_happy(130)
assert recursive_happy(97)

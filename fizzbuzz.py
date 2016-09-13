'''
Regras do FizzBuzz

1. Se a posição for multipla de 3: fizz
2. Se a posição for multipla de 5: buzz
3. Se a posição for multipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o proprio numero

'''

from functools import partial

import unittest

multiple_of = (lambda base, num: num % base == 0)
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif multiple_of_3(pos):
        say = 'fizz'

    return say


class FizzBuzzTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(robot(3), 'fizz')

# if __name__ == '__main__':
#     pass
    # unittest.main()
    # assert robot(1) == '1'
    # assert robot(2) == '2'
    # assert robot(4) == '4'

    # assert robot(3) == 'fizz'
    # assert robot(6) == 'fizz'
    # assert robot(9) == 'fizz'

    # assert robot(5) == 'buzz'
    # assert robot(10) == 'buzz'
    # assert robot(20) == 'buzz'

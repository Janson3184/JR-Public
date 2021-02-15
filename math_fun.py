'''Find a six digit perfect square whose last three digits is equal to the first three digits plus 1.'''

from math import sqrt
import numpy as np
import datetime

# TODO: start from perfect squares 316 to 1000 and go from there.  Much faster.

def is_perfect_square(number):
    square_root = float(sqrt(number))
    return square_root.is_integer()

def generate_six_digit_numbers(starting=100000, ending=999999):
    for i in range(starting, ending+1):
        yield i

generator = generate_six_digit_numbers()


def last_three_digits_equal_to_first_three_digits_plus_one(number):
    string_rep = str(number)

    first_three = string_rep[:3]
    last_three = string_rep[3:]

    first_three_int = int(first_three)
    last_three_int = int(last_three)

    return last_three_int == (first_three_int + 1)


def generate_perfect_squares(starting=316, ending=1000):
    for i in range(starting, ending+1):
        yield i**2

perfect_squares_generator = generate_perfect_squares()

# Doing what the problem asks for directly...i.e. "from finding a six digit perfect square"
s1 = datetime.datetime.now()
for number in generator:
    if is_perfect_square(number):
        if last_three_digits_equal_to_first_three_digits_plus_one(number):
            print(f'{number}')
e1 = datetime.datetime.now()

print(f'First iteration: {e1 - s1}')


# Figuring out the perfect squares backwards and iterating from that.
s2 = datetime.datetime.now()
for number in perfect_squares_generator:
    if last_three_digits_equal_to_first_three_digits_plus_one(number):
        print(number)
e2 = datetime.datetime.now()

print(f'Second iteration: {e2 - s2}')

print(f'As a ratio: {((e1-s1)/(e2-s2))}')


def sum_equals(*args,result):
    elements = [x for x in args]
    return sum(elements) == result

def product_equals(*args,result):
    elements = [x for x in args]
    return np.prod(elements) == result


sets = []

for i in range(4,41):
    for j in range(4,41):
        for k in range(4,41):
            if sum_equals(i,j,k,result=62) and product_equals(i,j,k,result=2880):
                if {i,j,k} not in sets:
                    sets.append({i,j,k})
print(sets)


import math


def gcd(a, b):
    while a:
        a, b = b % a, a
    return b


def const_different(variables, values):
    return len(values) == len(set(values))


def const_one_odd_one_even(variables, values):
    if values[0] % 2 == 0:
        return values[1] % 2 == 1
    else:
        return values[1] % 2 == 0


def const_smaller(variables, values):
    return values[0] < values[1]


def const_bigger(variables, values):
    return values[0] > values[1]


def const_squared_val(variables, values):
    if values[1] < 0:
        return False
    if values[0] < 0:
        return False
    return math.sqrt(values[1]) == values[0]


def const_gcd(variables, values):
    return gcd(values[0], values[1]) == 1


def const_sqrt_val(variables, values):
    if values[0] < 0:
        return False
    if values[1] < 0:
        return False
    return math.sqrt(values[0]) == values[1]


def const_divisible(variables, values):
    if values[1] == 0:
        return False
    return values[0] % values[1] == 0


def const_multiple(variables, values):
    if values[0] == 0:
        return False
    return values[1] % values[0] == 0


def const_double(variables, values):
    return values[1] == 2 * values[0]


def const_half(variables, values):
    return values[0] == 2 * values[1]


def def_constraints(edge, rand_number):
    const = ()
    opposite = const_different

    if rand_number == 1:
        const = (edge, const_different)
        opposite = const_different
    elif rand_number == 2:
        const = (edge, const_one_odd_one_even)
        opposite = const_one_odd_one_even
    elif rand_number == 3:
        const = (edge, const_smaller)
        opposite = const_bigger
    elif rand_number == 4:
        const = (edge, const_bigger)
        opposite = const_smaller
    elif rand_number == 5:
        const = (edge, const_squared_val)
        opposite = const_sqrt_val
    elif rand_number == 6:
        const = (edge, const_gcd)
        opposite = const_gcd
    elif rand_number == 7:
        const = (edge, const_sqrt_val)
        opposite = const_squared_val
    elif rand_number == 8:
        const = (edge, const_divisible)
        opposite = const_multiple
    elif rand_number == 9:
        const = (edge, const_multiple)
        opposite = const_divisible
    elif rand_number == 10:
        const = (edge, const_double)
        opposite = const_half
    return const, opposite

import math
import random

h_v = 1e-6
epsilon = 1e-18
chosen_i = 1


def f_d2(x, f_value):
    return (-f_value(x + 2 * h_v) + 16 * f_value(x + h_v) - 30 * f_value(x) + 16 * f_value(x - h_v) - f_value(
        x - 2 * h_v)) / (
                   12 * h_v * h_v)


def f_d1(x, i, f_value):
    if i == 1:
        return (3 * f_value(x) - 4 * f_value(x - h_v) + f_value(x - 2 * h_v)) / 2 * h_v
    if i == 2:
        return (-f_value(x + 2 * h_v) + 8 * f_value(x + h_v) - 8 * f_value(x - h_v) + f_value(x - 2 * h_v)) / (12 * h_v)


def f1(x):
    return (x ** 2) - 4 * x + 3


def f2(x):
    return x ** 2 + math.exp(1) ** x


def f3(x):
    return x ** 4 - 6 * (x ** 3) + 13 * (x ** 2) - 12 * x + 4


def compute_minimum(fun, lb1, ub1, lb2, ub2):
    x0 = random.uniform(lb1, ub1)
    x1 = random.uniform(lb2, ub2)
    x = x1
    h = x1 - x0
    k = 0
    delta_x = 0
    no = False
    while True:
        if abs(f_d1(x, chosen_i, fun) - f_d1(x - h, chosen_i, fun)) <= epsilon:
            no = True
            break
        delta_x = (h / (f_d1(x, chosen_i, fun) - f_d1(x - h, chosen_i, fun))) * f_d1(x, chosen_i, fun)
        x1 = x
        x = x - delta_x
        h = -delta_x
        k = k + 1
        if not (epsilon <= abs(delta_x) < 1e8 and k < 10000):
            break
    if no:
        return None, None
    else:
        if abs(delta_x) <= epsilon:
            return x, k
        else:
            print("Divergenta")
            return None, None


chosen_f = f1
it = 0
while True:
    it = it + 1
    xr, kr = compute_minimum(chosen_f, -10, 10, -10, 10)
    if xr is not None:
        print(
            "Punctul critic " + str(xr) + " gasit dupa " + str(it) + " iteratii ale calculului minimului, si " + str(
                kr) + " iteratii ale sirului")
        print("Derivata de ordin 2 in " + str(xr) + " este " + str(f_d2(xr, chosen_f)))

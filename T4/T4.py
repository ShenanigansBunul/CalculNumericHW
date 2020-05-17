import numpy as np
from math import sqrt


def read_rare(fname):
    f = open(fname, "r")
    f_arr = f.read().split('\n')
    f_size = int(f_arr[0])
    f_arr.pop(0)
    while '' in f_arr:
        f_arr.remove('')
    f.close()
    return f_arr, f_size


def read_list(fname):
    f = open(fname, "r")
    f_arr = f.read().split('\n')
    f_size = int(f_arr[0])
    f_arr.pop(0)
    while '' in f_arr:
        f_arr.remove('')
    f.close()
    return list(map(lambda x: float(x), f_arr)), f_size


a, a_size = read_rare("a_1.txt")
b, b_size = read_list("b_1.txt")


def empty_rare_matrix(n):
    result = []
    for _ in range(n):
        row = []
        result.append(row)
    return result


def rare_matrix(data, n):
    result = []
    for i in range(n):
        result.append([])
    for i in data:
        params = list(map(lambda x: float(x), i.split(',')))
        found = False
        for j in result[int(params[1])]:
            if j[1] == int(params[2]):
                found = True
                j[0] += params[0]
        if not found:
            result[int(params[1])].append([params[0], int(params[2])])
    return result


def diag_check(m, n):
    for i in range(n):
        found = False
        for j in m[i]:
            if j[1] == i:
                if j[0] != 0:
                    found = True
        if not found:
            return "Matricea nu are diagonala nenula"
    return "Matricea are diagonala nenula"


def get_diag(m, n):
    d = []
    for i in range(n):
        for j in m[i]:
            if j[1] == i:
                d.append(j[0])
    return d


def g_sum1(row, x, i):
    sum1 = 0.0
    for j in row:
        if j[1] <= i - 2:
            sum1 += j[0] * x[j[1]]
    return sum1


def g_sum2(row, x, n, i):
    sum2 = 0.0
    for j in row:
        if i < j[1] <= n:
            sum2 += j[0] * x[j[1]]
    return sum2


def gauss_seidel(m, b, n, x, d, delta):  # sistem m, termeni liberi b, dimensiune n, sir anterior x
    for i in range(n):
        row = m[i]
        new_x = (b[i] - g_sum1(row, x, i) - g_sum2(row, x, n, i)) / d[i]
        delta += pow(new_x - x[i], 2)
        x[i] = new_x
    return x, delta


def initial_x(n):
    result = []
    for i in range(n):
        result.append(i + 1)
    return result


def zeros(n):
    result = []
    for i in range(n):
        result.append(0)
    return result


a_matrix = rare_matrix(a, a_size)
print(diag_check(a_matrix, a_size))

x = zeros(a_size)
d = get_diag(a_matrix, a_size)
for _ in range(100000):
    delta = 0
    x, delta = gauss_seidel(a_matrix, b, a_size, x, d, delta)
    print(x[:10])
    if not (sqrt(delta) > 1e-32 and sqrt(delta) < 1e32):
        print("Divergenta")
        break

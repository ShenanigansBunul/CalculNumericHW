import numpy as np


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


a, a_size = read_rare("a_example.txt")
b, b_size = read_list("b_example.txt")


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

    result2 = []
    for i in range(n):
        result2.append(dict())
    for i in range(n):
        for j in result[i]:
            result2[i][str(j[1])] = j[0]
    return result2


def diag_check(m, n):
    for i in range(n):
        if str(i) not in m[i]:
            print(m[i])
            return "Matricea nu are diagonala nenula"
    return "Matricea are diagonala nenula"


def g_sum1(row, x, i):
    sum1 = 0
    for j in range(i-1):
        factor = 0
        if str(j) in row:
            factor = row[str(j)]
        sum1 += factor * x[j]
    return sum1


def g_sum2(row, x, n,  i):
    sum2 = 0
    for j in range(i, n):
        factor = 0
        if str(j) in row:
            factor = row[str(j)]
        sum2 += factor * x[j]
    return sum2


def gauss_seidel(m, b, n, x):  # sistem m, termeni liberi b, dimensiune n, sir anterior x
    new_x = zeros(n)
    for i in range(n):
        row = m[i]
        new_x[i] = (b[i] - g_sum1(row, new_x, i) - g_sum2(row, x, n, i)) / row[str(i)]
    return new_x


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

x = initial_x(a_size)
for i in range(25):
    x = gauss_seidel(a_matrix, b, a_size, x)
    print(x)

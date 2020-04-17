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
        non_null = False
        for j in m[i]:
            if j[1] == i:
                if j[0] != 0:
                    non_null = True
        if not non_null:
            return "Matricea nu are diagonala nenula"
    return "Matricea are diagonala nenula"


def gauss_seidel(m, x, b, n):  # sistem m, solutie x, termeni liberi b, dimensiune n
    for i in range(n):
        d = b[i]
        for j in range(n):
            if j != i:
                m_el = 0
                for k in m[i]:
                    if k[1] == j:
                        m_el = k[0]
                        break
                d = d - m_el * x[i]
        m_el = 0
        for k in m[i]:
            if k[1] == i:
                m_el = k[0]
                break
        x[i] = d / m_el
    return x


def initial_x(n):
    result = []
    for i in range(n):
        result.append(i+1)
    return result


a_1, a_1_size = read_rare("a_1.txt")
a_2, a_2_size = read_rare("a_2.txt")
a_3, a_3_size = read_rare("a_3.txt")
a_4, a_4_size = read_rare("a_4.txt")
a_5, a_5_size = read_rare("a_5.txt")
b_1, b_1_size = read_list("b_1.txt")
b_2, b_2_size = read_list("b_2.txt")
b_3, b_3_size = read_list("b_3.txt")
b_4, b_4_size = read_list("b_4.txt")
b_5, b_5_size = read_list("b_5.txt")

a_1_m = rare_matrix(a_1, a_1_size)
a_2_m = rare_matrix(a_2, a_2_size)
a_3_m = rare_matrix(a_3, a_3_size)
a_4_m = rare_matrix(a_4, a_4_size)
a_5_m = rare_matrix(a_5, a_5_size)

print(diag_check(a_1_m, a_1_size))
print(diag_check(a_2_m, a_2_size))
print(diag_check(a_3_m, a_3_size))
print(diag_check(a_4_m, a_4_size))
print(diag_check(a_5_m, a_5_size))

x = initial_x(a_1_size)

for i in range(25):
    x = gauss_seidel(a_1_m, x, b_1, a_1_size)

print(x)

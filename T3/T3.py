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


A_arr, A_size = read_rare("a.txt")
B_arr, B_size = read_rare("b.txt")
sum_test, sum_test_size = read_rare('aplusb.txt')
prod_test, prod_test_size = read_rare('aorib.txt')


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


def transpose(m, n):
    result = empty_rare_matrix(n)
    for i in range(n):
        for elem in m[i]:
            result[elem[1]].append([elem[0], i])
    return result


def rare_sum(m1, m2, n):
    result = m1.copy()
    for i in range(n):
        for j in range(len(m2[i])):
            found = False
            for k in range(len(result[i])):
                if result[i][k][1] == m2[i][j][1]:
                    result[i][k][0] += m2[i][j][0]
                    found = True
            if not found:
                result[i].append(m2[i][j])
    return result


def rare_product(m1, m2, n):
    result = empty_rare_matrix(n)
    m2_t = transpose(m2, n)
    for r_i in range(n):
        for r_j in range(n):
            s = 0
            for j in m1[r_i]:
                for k in m2_t[r_j]:
                    if j[1] == k[1]:
                        s += j[0] * k[0]
                        break
            if s != 0:
                result[r_i].append([s, r_j])
    return result


def sums(m, n):
    for i in range(n):
        new_el = []
        for el in m[i]:
            found = False
            for k in new_el:
                if k[1] == el[1]:
                    found = True
                    k[0] += el[0]
                    break
            if not found:
                new_el.append(el)
        m[i] = new_el


test_arr, test_size = read_rare("small_test.txt")
test = rare_matrix(test_arr, test_size)
test2_arr, test2_size = read_rare("small_test2.txt")
test2 = rare_matrix(test2_arr, test2_size)

A = rare_matrix(A_arr, A_size)
B = rare_matrix(B_arr, B_size)
sums(A, A_size)
sums(B, B_size)
A_plus_B = rare_sum(A, B, A_size)
A_plus_B_verify = rare_matrix(sum_test, sum_test_size)
A_ori_B = rare_product(A, B, A_size)
A_ori_B_verify = rare_matrix(prod_test, prod_test_size)

print(sorted(A_ori_B[0], key=lambda x: x[0]))
print(sorted(A_ori_B_verify[0], key=lambda x: x[0]))
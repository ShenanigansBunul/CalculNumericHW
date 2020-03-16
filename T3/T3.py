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
prod_text, prod_test_size = read_rare('aorib.txt')


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


A = rare_matrix(A_arr, A_size)
B = rare_matrix(B_arr, B_size)
A_plus_B = rare_sum(A, B, A_size)
A_plus_B_verify = rare_matrix(sum_test, sum_test_size)
print(A)
print(B)
print(A_plus_B)
print(A_plus_B_verify)

# cij: parcurs linia unei matrici (ez)
# pentru elementele nenule de pe pozitii linie m, n, p
# gasit elemente nenule de pe pozitii coloane m, n, p
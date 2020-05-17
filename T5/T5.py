import numpy as np
import random


def add_elem(s_m, x, y, v):
    for i in s_m[x]:
        if i[1] == y:
            return
    s_m[x].append([v, y])


def read_sparse(fname): # citit matrice rara din fisier
    f = open(fname, "r")
    f_arr = f.read().split('\n')
    f_size = int(f_arr[0])
    f_arr.pop(0)
    while '' in f_arr:
        f_arr.remove('')
    f.close()
    result = []
    for i in range(f_size):
        result.append([])
    for i in f_arr:
        params = list(map(lambda x: float(x), i.split(',')))
        found = False
        for j in result[int(params[1])]:
            if j[1] == int(params[2]):
                found = True
                j[0] += params[0]
        if not found:
            result[int(params[1])].append([params[0], int(params[2])])
    return result


def generate_random_sparse(s, ec, maxval): # generat matrice rara patratica aleatorie simetrica
    result = []
    for i in range(s):
        result.append([])
    for i in range(ec):
        c_x = random.randint(0, s - 1)
        c_y = random.randint(0, s - 1)
        v = random.randint(1, maxval)
        add_elem(result, c_x, c_y, v)
        add_elem(result, c_y, c_x, v)
    return result


q = generate_random_sparse(5, 1, 100)
print(q)
x = read_sparse("a_300.txt")
print(x)
# to do:
# metoda puterii pt aprox celei mai mari valori proprii a matricei A si un vector propriu apropiat
# se verifica simetrie, se afiseaza valorii proprii de modul maxim aproximate pt matrice aleatorie si pt cea din fisier
#
# caz p > n cu matrici NERARE: svd si afisat niste chestii
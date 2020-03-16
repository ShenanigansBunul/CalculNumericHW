import math
import numpy as np

eps = math.pow(10, -np.loadtxt('precision.txt'))
A = np.loadtxt('t2_large.txt')
b = np.loadtxt('t2_b_large.txt')
n = A.shape[0]
A_init = A.copy()
L = np.zeros((n, n))
# for i in range(n):
#     L[i][i] = 1
U = np.zeros((n, n))


def try_divide(a, b):
    if abs(b) > eps:
        return a / b
    else:
        print("Nu s-a putut face o impartire")
        return 0


def separate_triangles(A):
    loo = np.zeros((n,n))
    upp = np.zeros((n,n))
    for s in range(n):
        for t in range(n):
            if s == t:
                loo[s][t] = 1
                upp[s][t] = A[s][t]
            elif s > t:
                loo[s][t] = A[s][t]
            else:
                upp[s][t] = A[s][t]
    return loo,upp


def diagonal_determinant(m):
    result = 1
    for i in range(m.shape[0]):
        result *= m[i][i]
    return result


def l(c1, c2):  # daca calculam U si L in aceeasi matrice, pierdem diagonala lui L
    if c1 == c2:  # utilizam functia l in loc sa accesam elementul de pe linia c1, coloana c2
        return 1
    else:
        return A[c1][c2]

'''
for i in range(n):  # algoritmul de descompunere in doua matrici separate
    for k in range(i, n):  # popularea liniilor lui U
        s = 0
        for j in range(i):
            s = s + L[i][j] * U[j][k]
        U[i][k] = A[i][k] - s
    for k in range(i, n):  # popularea coloanelor lui L
        if i == k:
            L[i][i] = 1
        else:
            s = 0
            for j in range(i):
                s += (L[k][j] * U[j][i])
            L[k][i] = try_divide(A[k][i] - s, U[i][i])
'''

A = np.zeros((n, n))
for i in range(n):
    for k in range(i, n):
        s = 0
        for j in range(i):
            s = s + l(i, j) * A[j][k]
        A[i][k] = A_init[i][k] - s
    for k in range(i, n):
        if i != k:
            s = 0
            for j in range(i):
                s += (l(k, j) * A[j][i])
            A[k][i] = try_divide(A_init[k][i] - s, A[i][i])

L, U = separate_triangles(A)

print("Matricea U calculata de algoritmul ce se utilizeaza de mai multe matrici:")
print(U)
print("Matricea L calculata de algoritmul ce se utilizeaza de mai multe matrici:")
print(L)
print("Matricea calculata de algoritmul ce se utilizeaza de o singura matrice:")
print(A)
print("Determinantul lui A calculat obisnuit:")
print(np.linalg.det(A_init))
print("Determinantul lui A calculat stiind descompunerea LU:")
print(diagonal_determinant(L) * diagonal_determinant(U))


b_init = b.copy()
# rezolvam Ly = b
y = np.zeros(n)
for i in range(n):
    for j in range(i):
        b[i] = b[i] - y[j] * L[i][j]
    y[i] = b[i] / L[i][i]
# rezolvam Ux = y
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        y[i] = y[i] - x[j] * U[i][j]
    x[i] = y[i] / U[i][i]

print("Solutia sistemului Ax=b:")
print(x)
x_init = x.copy()
print("Calculam norma pentru a verifica solutia:")
print(np.linalg.norm(A_init.dot(x) - b_init, 2))

# calcul inversa matrice
A_inv = np.zeros((n, n))
for q in range(n):
    e = np.zeros(n)
    e[q] = 1
    # rezolvam Ly = b  -> Ly = e
    y = np.zeros(n)
    for i in range(n):
        for j in range(i):
            e[i] = e[i] - y[j] * L[i][j]
        y[i] = e[i] / L[i][i]
    # rezolvam Ux = y   -> Ux = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            y[i] = y[i] - x[j] * U[i][j]
        x[i] = y[i] / U[i][i]
    for q2 in range(n):
        A_inv[q2][q] = x[q2]

print("Calculam norma pentru a verifica solutia sistemului de ecuatii:")
alg_solution = np.linalg.solve(A_init, b_init)
print(np.linalg.norm(x_init - alg_solution, 2))

print("Norma xLU - A^-1 lib * b init:")
print(np.linalg.norm(x_init - np.linalg.inv(A_init).dot(b_init), 2))

print("Calculam norma pentru a verifica inversa:")
print(np.linalg.norm(A_inv - np.linalg.inv(A_init), 1))
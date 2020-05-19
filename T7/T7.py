from math import sqrt
import numpy as np
import random

epsilon = 1e-18


def sign(x):
    if x >= 0:
        return 1
    return -1


def d_params(p):
    result = []
    c = 0
    while c < len(p) - 1:
        result.append(p[c] * (len(p) - c - 1))
        c += 1
    return np.array(result)


class Polynomial:
    def solution_bounds(self):
        max_p = 0
        for i in self.params:
            if abs(i) > max_p:
                max_p = abs(i)
        r = (abs(self.params[0]) + max_p) / abs(self.params[0])
        self.lb = -abs(r)
        self.ub = abs(r)
        return -r, r

    def H(self, x):
        return ((self.degree - 1) ** 2) * (self.P1(x) ** 2) - self.degree * (self.degree - 1) * self.P(x) * self.P2(x)

    def P2(self, x):
        der = Polynomial(d_params(d_params(self.params)))
        return der.P(x)

    def P1(self, x):
        der = Polynomial(d_params(self.params))
        return der.P(x)

    def P(self, x):
        if len(self.params) == 0:
            return 0
        b = self.params[0]
        for i in range(1, len(self.params)):
            b = self.params[i] + b * x
        return b

    def compute_solution(self):
        x = random.uniform(self.lb, self.ub)
        k = 0
        delta_x = 0
        no = False
        while True:
            print(x)
            if self.H(x) < 0 or abs(self.P1(x) + sign(self.P1(x)) * sqrt(self.H(x))) <= epsilon:
                no = True
                break
            delta_x = self.degree * self.P(x) / (self.P1(x) + sign(self.P1(x)) * sqrt(self.H(x)))
            x = x - delta_x
            k = k + 1
            if not (1e-18 <= delta_x <= 1e8 and k <= 100000):
                break
        if no:
            print("Nu se poate continua sirul incepand de la x = " + str(x))
        else:
            if delta_x < epsilon:
                dup = False
                for i in self.solutions:
                    if abs(i - x) <= epsilon * 1e16:
                        dup = True
                if not dup:
                    self.solutions.append(x)
            else:
                print("Divergenta")

    def __init__(self, pars):
        self.lb = 0
        self.ub = 0
        self.solutions = []
        self.degree = len(pars) - 1
        self.params = pars
        self.solution_bounds()


poly = np.loadtxt('poly.txt')
p = Polynomial(poly)
for i in range(300):
    p.compute_solution()
print("Toate solutiile gasite sunt:")
print(p.solutions)
f = open("solutions.txt", "w")
for i in p.solutions:
    f.write(str(i) + "\n")
f.close()
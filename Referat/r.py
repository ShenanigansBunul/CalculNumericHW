import numpy as np

b_text = open("rhs1.txt", "r").read().split('\n')
a = np.loadtxt("sys1.txt")
b = np.loadtxt("rhs1.txt")
s = len(b)

x = np.linalg.solve(a, b)
print(x)
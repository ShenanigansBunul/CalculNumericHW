import random, math


def E1():
    print("Exercitiul 1:")
    m = 1
    u = pow(10, -m)
    while 1 + u != 1:
        m += 1
        u = pow(10, -m)
    print("1 + 10^-" + str(m) + " = " + str(u + 1))
    u = pow(10, -m + 1)
    print("1 + 10^-" + str(m - 1) + " = " + str(u + 1))


def E2():
    print("Exectitiul 2:")
    a = random.random()
    b = random.random()
    c = random.random()
    while (a * b) * c == a * (b * c):
        a = random.random()
        b = random.random()
        c = random.random()
    print("(" + str(a) + " * " + str(b) + ") * " + str(c) + " = " + str((a * b) * c))
    print(str(a) + " * (" + str(b) + " * " + str(c) + ") = " + str(a * (b * c)))
    u = pow(10, -15)
    print("(u + u) + 1 = " + str((u + u) + 1))
    print("u + (u + 1) = " + str(u + (u + 1)))
    print("(u * u) * 10 = " + str((u * u) * 10))
    print("u * (u * 10) = " + str(u * (u * 10)))


def empty_matrix(w, h):
    return [[0 for x in range(w)] for y in range(h)]


def partition_list(mat, vert):
    si = len(mat)
    m = math.floor(math.log(si, 2))
    c = 0
    result = []
    while c < si:
        if vert:
            elem = empty_matrix(m, si)
            for i, row in enumerate(elem):
                for j, elt in enumerate(row, start=c):
                    if j < len(mat):
                        elem[i][j - c] = mat[i][j]
            result.append(elem)
        else:
            elem = empty_matrix(si, m)
            for i, row in enumerate(elem, start=c):
                for j, elt in enumerate(row):
                    if i < len(mat):
                        elem[i - c][j] = mat[i][j]
            result.append(elem)
        c += m
    return result


def sum_b(mat):
    si = len(mat)
    sum_l = []
    for i in range(0, pow(2, si)):
        sum_el = empty_matrix(len(mat[0]), 1)[0]
        bs = format(i, '0' + str(si) + 'b')
        for j, row in enumerate(mat):
            if bs[len(bs) - j - 1] == "1":
                for k, elt in enumerate(row):
                    sum_el[k] += elt
        sum_l.append(sum_el)
    return sum_l


def num(row):
    result = 0
    for i, elem in enumerate(row):
        if elem > 0:
            result = result + pow(2, i)
    return result


def E3():
    print("Exerctitiul 3:")
    '''a = [[0, 0, 1, 1],
         [1, 0, 1, 0],
         [0, 1, 1, 1],
         [1, 1, 0, 1]]
    b = [[1, 1, 0, 1],
         [1, 0, 0, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 1]]'''
    a = [[0, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [0, 0, 1, 0, 1],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1]]
    b = [[1, 0, 0, 0, 1],
         [0, 1, 0, 0, 1],
         [0, 1, 1, 0, 0],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 0, 1]]
    si = len(a)
    # m = math.floor(math.log(si, 2))
    l_a = partition_list(a, True)
    l_b = partition_list(b, False)
    c_sum = empty_matrix(si, si)
    for i in range(len(l_a)):
        a_i = l_a[i]
        b_i = l_b[i]
        c = []
        sumb = sum_b(b_i)
        for j in range(len(a_i)):
            c.append(sumb[num(a_i[j])])
        for i1, co in enumerate(c):
            for i2, ro in enumerate(co):
                c_sum[i1][i2] += c[i1][i2]
    print("A * B: ")
    for i in range(len(c_sum)):
        for j in range(len(c_sum)):
            if c_sum[i][j] > 1:
                c_sum[i][j] = 1
        print(c_sum[i])


def main():
    E1()
    E2()
    E3()


if __name__ == "__main__":
    main()

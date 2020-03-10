import random
f = open("t2_b_large.txt", "w+")
for i in range(1):
    for j in range(100):
        f.write(str(random.randint(1, 20)))
        f.write(" ")
    f.write("\n")
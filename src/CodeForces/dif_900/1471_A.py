from sys import stdin
from math import ceil

t = int(stdin.readline())

for k in range(t):
    l1 = stdin.readline().split(" ")
    n = int(l1[0])
    x = int(l1[1])

    l2 = stdin.readline().split(" ")

    max = 0
    r = 0

    for i in l2:
        max += ceil(int(i) / x)
        r += int(i)

    print("{} {}".format(ceil(r / x), max))

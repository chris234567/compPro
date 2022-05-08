# local read from file

with open("C:/Users/Chris/VSCodeProjects/compPro/input.txt") as f:
    l = [_.replace("\n", "") for _ in f.readlines()]

a = [int(r) for r in l[1] if r != " "]

# read input from console

import sys

for k in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
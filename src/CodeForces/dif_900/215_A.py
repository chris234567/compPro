import sys

ls = []

for l in sys.stdin:
    ls.append(list(map(int, l.replace("\n","").split(" "))))

v = 0
c = 0

for fs in range(ls[0][0]):
    for rs in range(ls[2][0]):
        if ls[3][rs] % ls[1][fs] == 0:
            gear_ratio = int(ls[3][rs] / ls[1][fs])
            if v == gear_ratio:
                c += 1
            elif v < gear_ratio:
                v = gear_ratio
                c = 1

print(c)

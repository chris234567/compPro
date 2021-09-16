import sys

l = []

for k in sys.stdin:
    l.append(list(map(int, k.replace("\n","").split(" "))))

e = 0

for c in l[1]:
    if c % 2 == 0:
        e += 1

print(min(e, len(l[1]) - e))
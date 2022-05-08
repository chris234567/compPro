import sys

sys.stdin.readline()
a = [int(r) for r in sys.stdin.readline().replace("\n", "").split(" ")]

m = []
l = 0

if (a.count(max(a)) == len(a)):
    print(len(a))
else:
    for i in a:
        if i == max(a):
            l += 1
        else:
            m.append(l)
            l = 0
    else:
        m.append(l)

    print(max(m))

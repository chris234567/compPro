import sys

for k in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    s = 0
    m = 0
    l = 0
    
    if n < 6:
        print(15)
        continue

    r = n % 6
    s += int(n / 6)

    if r == 5:
        s += 1
    elif r == 1 or r == 2:
        m += 1
        s -= 1
    elif r == 3 or r == 4:
        l += 1
        s -= 1

    t = s * 15 + m * 20 + l * 25
    print(t)
        
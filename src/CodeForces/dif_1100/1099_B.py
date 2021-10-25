import sys
from math import sqrt

q = int(sys.stdin.readline())
s = sqrt(q)

if s % 1 == 0:
    print(int(2 * s))
else:
    s = int(s // 1 + 1)
    if q <= s * s - s:
        print(2 * s - 1)
    else:
        print(2 * s)
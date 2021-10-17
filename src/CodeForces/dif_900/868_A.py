import sys

pwd = sys.stdin.readline()
sequence = []

for k in range(int(sys.stdin.readline())):
    sequence.append(sys.stdin.readline())

def solve():
    if pwd in sequence:
        print("YES")
        return

    for b in sequence:
        if b[1] == pwd[0]:
            for c in sequence:
                if c[0] == pwd[1]:
                    print("YES")
                    return

    print("NO")

solve()
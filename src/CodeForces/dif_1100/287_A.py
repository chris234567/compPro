import sys

field = []
symb = ["#", "."]

for i in range(4):
    field.append(sys.stdin.readline().replace('\n', ''))

def iq_test():
    for y in range(0, 2):
        for x in range(0, 2):
            for s in symb:
                if field[y][x] == s and field[y][x + 1] == s:
                    if field[y + 1][x] == s and field[y + 1][x + 1] == s:
                        return "YES"
    for s in symb:
        for i in range(4 * 4):
            field[i // 4][i % 4] = s

    for y in range(0, 2):
        for x in range(0, 2):
            for s in symb:
                if field[y][x] == s and field[y][x + 1] == s:
                    if field[y + 1][x] == s and field[y + 1][x + 1] == s:
                        return "YES"

    return "NO"

print(iq_test())


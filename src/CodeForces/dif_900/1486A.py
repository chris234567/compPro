# import sys

# ls = []

# for l in sys.stdin:
#     ls.append(list(map(int, l.replace("\n","").split(" "))))

with open("C:\\Users\\Chris\\VSCodeProjects\\compPro\\src\\CodeForces\\dif_900\\input.txt") as file:
    ls = file.readlines()

lines = []

for line in ls:
    lines.append(list(map(int, line.replace("\n","").split(" "))))

cases = lines[0][0]

for case in range(0, cases * 2, 2):
    towers = lines[case + 2]
    strict_increase = True

    for i in range(0, len(towers) - 1):
        move_possible = True

        if towers[i] == towers[i + 1] - 1:
            move_possible = False

        if towers[i] < towers[i + 1]:
            continue

        if towers[i] > towers[i + 1] + 1:
            print("No")
            strict_increase = False
            break

        if towers[i] >= towers[i + 1]:
            if not move_possible:
                print("No")
                strict_increase = False
                break

            towers[i] -= 1
            towers[i + 1] += 1
            
    if strict_increase:
        print("Yes")

        

with open('cases.txt') as f:
    file = f.readlines()

cases = int(file[0].replace('\n', ' '))

def calc(max_str):
    count = 0
    for l in range(1, len(max_str)):
        count += (10 ** l) * (1/2) ** l  # 999 -> 1000 pro stelle mal 1/2 plus 100 pro stelle mal 1/2 plus 10 ... plus 5

    return count      

def calc2(max_str):
    odd = True
    first = True
    boring = 0
    cnt = 0

    for pos in max_str:
        pos = int(pos)  # first digit from the left
        cnt += 1

        if pos == 0:  # ACHTUNG MUSS GEFIXT werdn + spezialfall z.b 10
            if odd:
                break

        if cnt == len(max_str):  # last digit
            if odd:
                boring += int(pos / 2) + ((pos / 2) %  1 > 0)
            else:
                boring += int(pos / 2) + 1
        else:
            if first:  # FUNKTIONIERT nix aendern pls
                boring += calc(max_str)  # 999 -> 1000 pro stelle mal 1/2 plus 100 pro stelle mal 1/2 plus 10 ... plus 5  
                first = False
            
            for k in range(2, pos):
                if (k - 1) % 2 == odd:   # eeehhhh
                    boring += calc(max_str)


            odd = not odd  # alternate

    return boring

for i in range(cases):
    max_str = file[i + 1].split(' ')[1].replace('\n', '')
    odd = True
    first = True
    boring = 0
    cnt = 0

    for pos in max_str:
        pos = int(pos)  # first digit from the left
        cnt += 1

        if pos % 2 != odd:
            if len(max_str) > 2:
                boring += calc2(str((10 ** (cnt - 1)) - 1))
                break

        if pos == 0:  # ACHTUNG MUSS GEFIXT werdn + spezialfall z.b 10
            if odd:
                break

        if cnt == len(max_str):  # last digit
            if odd:
                boring += int(pos / 2) + ((pos / 2) %  1 > 0)
            else:
                boring += int(pos / 2) + 1
        else:
            if first:  # FUNKTIONIERT nix aendern pls
                boring += calc(max_str)  # 999 -> 1000 pro stelle mal 1/2 plus 100 pro stelle mal 1/2 plus 10 ... plus 5  
                first = False
            
            for k in range(2, pos):
                if (k - 1) % 2 == odd:   # eeehhhh
                    boring += calc(max_str)

            odd = not odd  # alternate

    print('Case #{}: {}'.format(i + 1, boring))

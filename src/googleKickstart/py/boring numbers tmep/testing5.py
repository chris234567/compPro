with open('cases.txt') as f:
    file = f.readlines()

cases = int(file[0].replace('\n', ' '))

for i in range(cases):
    max_str = file[i + 1].split(' ')[1].replace('\n', '')
    boring = 0
    odd = False
    once = True

    for r in range(len(max_str)):
        curr_pos = int(max_str[0])  # first digit from the left
        odd = not odd  # alternate

        if curr_pos == 0:  # ACHTUNG MUSS GEFIXT werdn + spezialfall z.b 10
            max_str = max_str[1::] # 999 -> 99
            continue

        cnt = 0

        if odd:
            cnt = int(curr_pos / 2) + ((curr_pos / 2) %  1 > 0) - 1
        else:
            cnt = int(curr_pos / 2)

            if len(max_str) > 4:
                boring += 5 ** (len(max_str) - 4)

        if len(max_str) == 1:  # last digit
            boring += cnt + 1  # +1 cause of 0
        elif cnt > 0:
            # always => n - 1
            boring += 5 ** (len(max_str) - 1)
            if len(max_str) > 2:
                boring += 5

            if len(max_str) > 2:
                boring += cnt * (5 ** (len(max_str) - 1) + 5)
            else:
                boring += cnt * (5 ** (len(max_str) - 1))

        if odd:
            if curr_pos % 2 != 1:
                break
        else:
            if curr_pos % 2 != 0:
                break

        max_str = max_str[1::] # 999 -> 99

    print('Case #{}: {}'.format(i + 1, boring))

with open('cases.txt') as f:
    file = f.readlines()

cases = int(file[0].replace('\n', ' '))

for i in range(cases):
    max_str = file[i + 1].split(' ')[1].replace('\n', '')
    odd = True
    first = True
    boring = 0

    for r in enumerate(max_str):
        curr_pos = int(max_str[0])  # first digit from the left

        if curr_pos == 0:  # ACHTUNG MUSS GEFIXT werdn + spezialfall z.b 10
            if odd:
                break

        if odd:
            cnt = int(curr_pos / 2) + ((curr_pos / 2) %  1 > 0) - 1
        else:
            cnt = int(curr_pos / 2)

        if len(max_str) == 1:  # last digit
            boring += cnt + 1  # +1 cause of 0
        else:
            if first:
                cnt += 1
                first = False
                
            for l in range(1, len(max_str)):
                boring += cnt * (10 ** l) * (1/2) ** l  # 999 -> 1000 pro stelle mal 1/2 plus 100 pro stelle mal 1/2 plus 10 ... plus 5

            if curr_pos % 2 != odd:
                break

            max_str = max_str[1::] # 999 -> 99
            odd = not odd  # alternate

    print('Case #{}: {}'.format(i + 1, boring))

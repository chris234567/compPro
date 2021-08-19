with open('cases.txt') as f:
    file = f.readlines()

cases = int(file[0].replace('\n', ' '))

for i in range(cases):
    max_str = file[i + 1].split(' ')[1].replace('\n', '')
    boring = 0

    odd_nums = [1, 3, 5, 7, 9]
    even_nums = [0, 2, 4, 6, 8]

    odd = False

    for r in range(len(max_str)):
        curr_pos = int(max_str[0])  # first digit from the left
        odd = not odd  # alternate

        if curr_pos == 0:
            max_str = max_str[1::] # 999 -> 99
            continue

        cnt = 0

        for k in range(1, curr_pos):
            if odd:
                if k in odd_nums:
                    cnt += 1
            else:
                if k in even_nums:
                    cnt += 1

        if len(max_str) == 1:  # last digit
            boring += cnt + 1  # +1 cause of 0
        else:
            if cnt > 0:
                # always => n - 1
                boring += (5 ** (len(max_str) - 1))
                if (len(max_str) > 2):
                    boring += 5

                boring += cnt * (5 ** (len(max_str) - 1))
                if (len(max_str) > 3):
                    boring += cnt * 5

        if odd:
            if curr_pos % 2 != 1:
                break
        else:
            if curr_pos % 2 != 0:
                break

        max_str = max_str[1::] # 999 -> 99

    print(boring)
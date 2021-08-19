import time, math

t0 = time.time()
with open('cases.txt') as f:
    file = f.readlines()

cases = int(file[0].replace('\n', ' '))

for i in range(cases):
    boring = 0
    min = int(file[i + 1].split(' ')[0].replace('\n', ' '))
    max = int(file[i + 1].split(' ')[1].replace('\n', ' '))
    k = min

    while True:
        digits = int(math.log10(k)) + 1
        start = 1
        boringBool = True

        for l in range(digits, 0, -1):
            if not (k // (10 ** (l - 1))) % 2 == start % 2:
                boringBool = False
                r = l
                break

            start = (start + 1) % 2

        if k > max:
            break

        if boringBool: 
            boring += 1
            # print(k)
            if digits == int(math.log10(k + 1)) + 1:
                k += 2
            else:
                k += 1
            continue
        
        k = k // (10 ** (r - 1))
        k = k * (10 ** (r - 1))
        k += (10 ** (r - 1))

    print('Case #{}: {}'.format(i + 1, boring))

t1 = time.time()
print (t1 - t0)

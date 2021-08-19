import math, time

start = 0

def func(max):
    if (max == 0): return 0

    k = int(math.log10(max)) + 1
    global start
    start = (start + 1) % 2 # "position" indicator
    boring = 0

    if (k == 1):
        count = 0
        for l in range(start, 10, 2):
            if l <= max % (10 ** (k)):
                count += 1
        boring += count
    else:
        count = 0
        for l in range(start, 10, 2):
            if l <= max // (10 ** (k - 1)):
                count += 1

        boring += count * (5 ** (k - 1))
        
        # if (max % (10 ** (k - 1)) < k - 1 and k > 2): # meh
        #     boring += func(10 ** (k - 2) + (max % (10 ** (k - 1))))
        # else:
        
        boring += func(max % (10 ** (k - 1)))

    return boring


t0 = time.time()
with open('cases.txt') as f:
    file = f.readlines()

cases = int(file[0].replace('\n', ' '))

for i in range(cases):
    min = int(file[i + 1].split(' ')[0].replace('\n', ' '))
    max = int(file[i + 1].split(' ')[1].replace('\n', ' '))
    min = func(min)
    start = 0
    max = func(max) 
    boring = max - min
    print('Case #{}: {}'.format(i + 1, boring))

t1 = time.time()
print (t1 - t0)
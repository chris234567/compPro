with open('cases.txt') as f:
    file = f.readlines()

cases = int(file[0].replace('\n', ' '))

for i in range(cases):
    boring = 0
    min = int(file[i + 1].split(' ')[0].replace('\n', ' '))
    max = int(file[i + 1].split(' ')[1].replace('\n', ' '))
    r = min

    for k in range(max - min + 1):
        counter = 0
        
        for l in range(len(str(r))):
            if (int(str(r)[l]) % 2 == (l + 1) % 2):
                counter += 1

        if (counter == len (str(r))):
            boring += 1
        
        r += 1

    print('Case #{}: {}'.format(i + 1, boring))
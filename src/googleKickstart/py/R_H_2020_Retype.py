cases = int(input())

for i in range(cases):
    nums = input().split(' ')
    
    lvlAll = int(nums[0]) + 1
    lvlCurr = int(nums[1]) - 1
    lvlSword = int(nums[2])
    time = lvlCurr + lvlAll

    turnBack = (lvlCurr + 1 - lvlSword) + (lvlAll - lvlSword)

    if (turnBack < lvlAll):
        time = lvlCurr + turnBack

    print('Case #{}: {}'.format(i + 1, time))
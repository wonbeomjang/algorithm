from itertools import permutations

n = int(input())

elements = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '666']
nums = []

for i in range(1, 12):
    for element in permutations(elements, i):
        num = ''.join(element)
        print(num)
        if not '666' in num:
            continue
        nums += [num]
nums = list(set(map(int, nums)))
nums.sort()

print(nums)
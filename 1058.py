from sys import stdin

nums = list(map(int, stdin.readline().split()))

nums.sort()

for i in range(nums[0], nums[0] * nums[1] * nums[2] + 1):
    cnt = 0
    for num in nums:
        if i % num == 0:
            cnt += 1
            
    if cnt >= 3:
        print(i)
        break

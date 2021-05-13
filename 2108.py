from sys import stdin
from collections import Counter

input = stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]

nums.sort()
num_dic = Counter(nums)
num_dic = sorted(num_dic.items(), key=lambda item: item[1], reverse=True)

print(round(sum(nums) / len(nums)))
print(nums[len(nums) // 2])

if N != 1 and num_dic[0][1] == num_dic[1][1]:
    print(num_dic[1][0])
else:
    print(num_dic[0][0])

print(nums[-1] - nums[0])

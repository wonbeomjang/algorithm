digits = {}

n = int(input())

for i in range(n):
    nums = input()
    
    for j in range(len(nums)):
        if nums[j] in digits:
            digits[nums[j]] += 10 ** (len(nums) - j - 1)
        else:
            digits[nums[j]] = 10 ** (len(nums) - j - 1)

nums = sorted(digits.items(), key=lambda item: item[1], reverse=True)

ans = 0
for i, (alphabet, summation) in enumerate(nums):
    ans += summation * (9 - i)

print(ans)
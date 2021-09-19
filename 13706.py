n = int(input())

left = 0
right = n
mid = 1

while left < right:
    mid = (left + right) // 2
    
    if mid ** 2 < n:
        left = mid + 1
    else:
        right = mid

print(right)
        
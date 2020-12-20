s = int(input())

ls = []
summation = 0

for i in range(1, 100002):
    summation += i
    ls += [summation]

l, r = 0, 100000

while l <= r:
    mid = (l + r) // 2
    
    if s < ls[mid]:
        r = mid - 1
    else:
        l = mid + 1
    
    print(l, mid, r, s ,ls[mid])

print(l)
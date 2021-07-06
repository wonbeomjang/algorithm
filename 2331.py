import sys

input = lambda: sys.stdin.readline().strip()

a, p = map(int, input().split())

arr = set()
# arr = []

recent = a

def calc(recent):
    res = 0
    
    while recent:
        res += (recent % 10) ** p
        recent //= 10
        
    return res

while not recent in arr:
    arr.add(recent)
    # arr += [recent]
    recent = calc(recent)

while recent in arr:
    arr.remove(recent)
    recent = calc(recent)
    
print(len(arr)
import sys

input = lambda: sys.stdin.readline().strip()

num_crane = int(input())
crane_weight = sorted(list(map(int, input().split())), reverse=True)
num_box = int(input())
box_weight = sorted(list(map(int, input().split())), reverse=True)

if box_weight[0] > crane_weight[0]:
    print(-1)
    exit()
    
res = 0
while box_weight:
    res += 1
    for c in crane_weight:
        for i in range(len(box_weight)):
            if box_weight[i] <= c:
                del box_weight[i]
                break
            
print(res)
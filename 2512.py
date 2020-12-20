N = int(input())

required = list(map(int, input().split()))

total_money = int(input())

start = 0
end = max(required)

while start <= end:
    upper_bound = (start + end) // 2
    req_sum = 0
    for req in required:
        if req < upper_bound:
            req_sum += req
        else:
            req_sum += upper_bound
        
    if total_money < req_sum:
        end = upper_bound - 1
    else:
        start = upper_bound + 1
            
print(end)
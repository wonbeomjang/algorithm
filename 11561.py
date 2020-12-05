num_tests = int(input())

for _ in range(num_tests):
    N = int(input())
    
    ans = 10 ** 16
    i = 0
    
    while(True):
        if ans * (ans - 1) / 2 <= N < ans * (ans + 1) / 2:
            print(ans - 1)
            break
        
        if ans * (ans - 1) / 2 > N:
            ans = ans // 2
    
    for i in range(ans):
        if N < i * (i + 1) / 2:
            print(i - 1)
            break
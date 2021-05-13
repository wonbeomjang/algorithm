N, K = map(int, input().split())

def solved():
    global N, K
    res = 0
    
    while True:
        tempN = N
        cnt = 0
        
        while tempN:
            if tempN % 2:
                cnt += 1
            tempN //= 2
            
        if cnt <= K:
            print(res)
            return
        
        N += 1
        res += 1

solved()
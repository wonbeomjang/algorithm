N = int(input())
state = False
elements = list(map(str, range(10)))

nums = [[], [], [], [], [], [], [], [], [], []]

if N < 1024:
    for i in range(1, 1 << 10):
        num = ""
        cnt = 0
        for j in range(10):
            if (i & 1 << j):
                num = elements[j] + num
                cnt += 1
            nums[cnt - 1].append(num)
        cnt = 0
        
        for e in nums:
            if state:
                break
            for n in e:
                cnt += 1
                if cnt == N:
                    state = True
                    print(n)
                    break
                
else:
    print(-1)
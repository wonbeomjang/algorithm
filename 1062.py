from sys import stdin

N, K = map(int, stdin.readline().split())

words = []
for _ in range(N):
    words += [stdin.readline()[4:-5]]

visited = [False for _ in range(26)]

visited[ord('a') - ord('a')] = True
visited[ord('c') - ord('a')] = True
visited[ord('i') - ord('a')] = True
visited[ord('n') - ord('a')] = True
visited[ord('t') - ord('a')] = True

res = 0

def learned(alphabet, num_learned):
    global visited
    global K
    global res
    
    if num_learned == K:
        cnt = 0
        
        for i in range(N):
            for j in range(len(words[i])):
                if not visited[ord(words[i][j]) - ord('a')]:
                    break
            else:
                cnt += 1
                
        res = max(res, cnt)
        
    else:
        for a in range(alphabet, 26):
            if not visited[a]:
                visited[a] = True
                learned(a, num_learned + 1)
                visited[a] = False
            
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    K -= 5
    learned(0, 0)
    print(res)
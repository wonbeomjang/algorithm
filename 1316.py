num_word = int(input())

cnt = 0

for i in range(num_word):
    visited = [False for _ in range(26)]
    flag = True
    word = input()
    
    visited[ord(word[0]) - ord('a')] = True
    
    for i in range(1, len(word)):
        if word[i - 1] == word[i]:
            continue
        
        if visited[ord(word[i]) - ord('a')]:
            break
        
        visited[ord(word[i]) - ord('a')] = True
    else:
        cnt += 1
        
print(cnt)
        
    
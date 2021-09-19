def solution(strs, t):
    dp = [float('inf')] * (len(t) + 1)
    strs = set(strs)
    dp[0] = 0
    for i in range(len(t)):
        for j in range(1, 6):
            if i + j <= len(t) and t[i: i + j] in strs:
                dp[i + j] = min(dp[i + j], dp[i] + 1)
            
    
    print(dp)
    return 0
    
print(solution(["ba","na","n","a"], "banana"))
print(solution(["app","ap","p","l","e","ple","pp"], "apple"))
print(solution(["ba","an","nan","ban","n"], "banana"))
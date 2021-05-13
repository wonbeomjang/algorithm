from collections import Counter

def solve():
    number = Counter(input())
    
    cnt = 0
    center_latter = ''
    for v in number:
        if number[v] % 2:
            cnt += 1
            center_latter = v
    
    if cnt > 1:
        print("I'm Sorry Hansoo")
        return
    
    
    alphabet = sorted(number.items())
    
    string = ''
    
    for a, num in alphabet:
        string += a * (num // 2)
        
    string = string + center_latter + string[::-1]
    print(string)
    
    
solve()
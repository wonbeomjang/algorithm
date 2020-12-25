L, C = map(int, input().split())
alphabets = set(input().split())

consonant = alphabets - {'a', 'e', 'i', 'o', 'u'}
vowel = alphabets.intersection({'a', 'e', 'i', 'o', 'u'})
alphabets = sorted(list(alphabets))

def dfs(index, string, num_cons, num_vow):
    global consonant
    global vowel
    global L
    
    if num_cons + num_vow == L:
        if num_cons >= 2 and num_vow >= 1:
           print(string)
           return
        else:
            return
    if index == C:
        return
    
    a = alphabets[index]
    if a in vowel:
        dfs(index + 1, string + a, num_cons, num_vow + 1)
    else:
        dfs(index + 1, string + a, num_cons + 1, num_vow)
    dfs(index + 1, string, num_cons, num_vow)
dfs(0, "", 0, 0)
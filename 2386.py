from sys import stdin

while True:
    string = stdin.readline()
    alphabet = string[0]
    cnt = 0
    
    if alphabet == '#':
        break
    
    string = string[2:]
    for s in list(string):
        if alphabet.lower() == s.lower():
            cnt += 1
    
    print(f'{alphabet} {cnt}')
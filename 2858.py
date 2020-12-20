from sys import stdin, stdout

def sol(r, b):
    total_tile = r + b
    for w in range(3, total_tile):
        if total_tile % w != 0:
            continue
        l = total_tile // w
        if not w <= l:
            continue
        
        expected_r = 2 * (w + l) - 4
        expected_b = (w - 2) * (l - 2)
        
        if expected_r == r and expected_b == b:
            print(l, w)
            return
        

r, b = map(int, stdin.readline().split())

sol(r, b)
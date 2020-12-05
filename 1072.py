numGames, numWins = map(int, input().split(' '))

z = int(numWins / numGames * 100)

l, r = 0, 1000000000

while l < r:
    mid = (l + r) // 2
    newZ = int((numWins + mid) * 100 / (numGames + mid))
    
    if z < newZ:
        r = mid
    else:
        l = mid + 1
    print(l, mid, r, z, newZ)
    
if z >= 99:
    print(-1)
else:
    print(mid)
    
    
    
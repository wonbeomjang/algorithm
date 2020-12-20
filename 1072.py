numGames, numWins = map(int, input().split(' '))

z = int(numWins * 100 / numGames)

l, r = 0, 1000000000

while l <= r:
    mid = (l + r) // 2
    newZ = int((numWins + mid) * 100 / (numGames + mid))
    
    if newZ > z:
        r = mid - 1
    else:
        l = mid + 1
    
if z >= 99:
    print(-1)
else:
    print(l)
    
    
    
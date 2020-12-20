numNotHeard, numNotSeen = map(int, input().split())

notHeardList = []
notSeenList = []

for i in range(numNotHeard):
    notHeardList += [input()]

for i in range(numNotSeen):
    notSeenList += [input()]

notHeardList = set(notHeardList)
notSeenList = set(notSeenList)

notHeardAndNotSeen = sorted(notHeardList.intersection(notSeenList))

print(len(notHeardAndNotSeen))

for p in notHeardAndNotSeen:
    print(p)

    
    
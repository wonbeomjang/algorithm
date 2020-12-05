pole = {'0': 'N', '1': 'S'}

class Gear:
    def __init__(self, status: str):
        self.status = []
        for i in range(len(status)):
            self.status += [pole[status[i]]]
    
    def getLeftPole(self) -> str:
        return self.status[-2]
    
    def getRightPole(self) -> str:
        return self.status[2]
    
    def getTopPole(self) -> str:
        return self.status[0]
        
    def rotateClockWise(self):
        temp = self.status[-1]
        del self.status[-1]
        self.status = [temp] + self.status
        
    def rotateCounterClockWise(self):
        temp = self.status[0]
        del self.status[0]
        self.status = self.status + [temp]
        
    def __str__(self) -> str:
        return str(self.status)

def check_right(index, direction):
    if index > 4 or gears[index - 1].getRightPole() == gears[index].getLeftPole():
        return
    check_right(index + 1, -direction)
    
    if direction == 1:
        gears[index].rotateClockWise()
    else:
        gears[index].rotateCounterClockWise()

def check_left(index, direction):
    if index < 1 or gears[index + 1].getLeftPole() == gears[index].getRightPole():
        return
    check_left(index - 1, -direction)
    
    if direction == 1:
        gears[index].rotateClockWise()
    else:
        gears[index].rotateCounterClockWise()
        


gears = {}    
for i in range(1, 5):
    status = input()
    gears[i] = Gear(status)

numCommands = int(input())

for _ in range(numCommands):
#    for i in range(1, 5):
#        print(gears[i])
#    print()
    num, direction = map(int, input().split(' '))
    directionTemp = direction
    
    check_right(num + 1, -direction)
    check_left(num - 1, -direction)
    
    if direction == 1:
        gears[num].rotateClockWise()
    else:
        gears[num].rotateCounterClockWise()
   
        
score = 0

for i in range(1, 5):
#    print(gears[i])
    if gears[i].getTopPole() == 'S':
        score += 2 ** (i - 1)

print(score)

"""
['S', 'N', 'S', 'N', 'S', 'S', 'S', 'S']
['N', 'S', 'S', 'S', 'S', 'S', 'N', 'S']
['S', 'S', 'N', 'N', 'S', 'S', 'S', 'N']
['N', 'N', 'N', 'N', 'N', 'N', 'S', 'N']
"""
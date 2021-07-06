import sys

class Grid:
    grid = {}
    cnt = 0
    
    def __init__(self, num_grid):
        self.num_grid = num_grid
    
    def recommend(self, num):
        self.cnt += 1
        
        if num in self.grid:
            self.grid[num] = (self.grid[num][0] + 1, self.grid[num][1])
            return
        
        if len(self.grid) >= self.num_grid:
            drop_num, _ = sorted(self.grid.items(), key=lambda item: item[1])[0]
            del self.grid[drop_num]
        
        self.grid[num] = (1, self.cnt)
        
    def __str__(self):
        keys = []
        for k in self.grid.keys():
            keys += [k]
        keys.sort()
        
        return ' '.join(map(str, keys))
        
        

input = lambda: sys.stdin.readline().strip()

num_grid = int(input())
num_recommend = int(input())
recommends = list(map(int, input().split()))

grid = Grid(num_grid)

for r in recommends:
    grid.recommend(r)
    
print(grid)

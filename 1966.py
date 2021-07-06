import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

num_tests = int(input())

class PrinterQueue():
    q = deque()
    
    def __init__(self, priorities):
        for i, p in enumerate(priorities):
            self.q.append((i, p))
            self.priorities = priorities
    
    def reset(self):
        self.q.clear()
        
    def pop(self):
        length = len(self.q)
        for i in range(length):
            num, p = self.q.popleft()
            
            
            if not self.q or p == max(self.priorities):
                self.priorities.remove(p)
                return num
            else:
                self.q.append((num, p))
        

for i in range(num_tests):
    num_documents, docs = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    printer_queue = PrinterQueue(priorities)
    i = 1
    
    while docs != printer_queue.pop():
        i += 1
        
    print(i)
    printer_queue.reset()
    
    
    
    
    



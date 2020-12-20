from math import sqrt

x, y, c = map(float, input().split())

def get_expected_c(d: int):
    global x
    global y
    h1 = sqrt(x*x - d*d)
    h2 = sqrt(y*y - d*d)
    
    return (h1*h2) / (h1+h2)

start = 0
end = min(x, y)

while(end - start > 1e-4):
    mid = (start + end) / 2.0
    expected_c = get_expected_c(mid)
    
    if c < expected_c:
        start = mid
    else:
        end = mid
        
        
print(f'{start:.3f}')
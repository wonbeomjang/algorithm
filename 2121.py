def get_num_blueRay(lessons_length, each_length):
    summation = 0
    expected_blueRay = 0
    
    for length in lessons_length:
        if each_length < summation + length:
            expected_blueRay += 1
            summation = 0
            
        summation += length
    if summation:
        expected_blueRay += 1
    
    return expected_blueRay

num_lessons, num_blueRay = map(int, input().split())

lessons_length = list(map(int, input().split()))

start = max(lessons_length)
end = sum(lessons_length)

while start <= end:
    mid = (start + end) // 2
    
    expected_num = get_num_blueRay(lessons_length, mid)
    
    if expected_num <= num_blueRay:
        end = mid - 1
    else:
        start = mid + 1
        
print(start)
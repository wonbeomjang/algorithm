def solution(k, room_number):
    answer = []
    
    delta = [0 for i in range(k + 1)]
    print(len(delta))
    for num in room_number:
        if not delta[num]:
            answer += [num]
            delta[num] = 1
        else:
            for i in range(delta[num], k):
                nextRoom = num + i
                if not delta[nextRoom]:
                    answer += [nextRoom]
                    delta[nextRoom] = 1
                    delta[num] += i
        
    return answer
    
k = int(input())
room_number = list(input())

print(solution(k, room_number))
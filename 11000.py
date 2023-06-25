import heapq

num_classes = int(input())
schedule = sorted([tuple(map(int, input().split())) for i in range(num_classes)])

meeting_room = [schedule[0][1]]
del schedule[0]

for start, end in schedule:
    fastest_end_time = heapq.heappop(meeting_room)
    if fastest_end_time <= start:
        heapq.heappush(meeting_room, end)
    else:
        heapq.heappush(meeting_room, fastest_end_time)
        heapq.heappush(meeting_room, end)

print(len(meeting_room))

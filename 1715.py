import heapq

num_cards = int(input())
cards = [int(input()) for i in range(num_cards)]
heapq.heapify(cards)

cnt = 0
while len(cards) != 1:
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)
    res = c1 + c2
    cnt += res
    heapq.heappush(cards, res)

print(cnt)


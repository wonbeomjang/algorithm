import sys

input = lambda: sys.stdin.readline().strip()

def solve():
    max_num = int(input()) - 1
    money_info = sorted(list(enumerate(map(int, input().split()))), key=lambda x: x[1])
    num2cost = {k: v for k, v in money_info}
    money = int(input())

    result = []

    if money_info[0][0] == 0:
        if max_num == 0 or money_info[1][1] > money:
            return "0"
        result += [money_info[1][0]]
        money -= money_info[1][1]
    else:
        result += [money_info[0][0]]
        money -= money_info[0][1]

    while money - money_info[0][1] >= 0:
        result += [money_info[0][0]]
        money -= money_info[0][1]

    money_info.sort(key=lambda x: x[0], reverse=True)

    for val, cost in money_info:
        for i in range(len(result)):
            if result[i] < val and cost - num2cost[result[i]] <= money:
                money = money - cost + num2cost[result[i]]
                result[i] = val


    return "".join(map(str, result))

print(solve())
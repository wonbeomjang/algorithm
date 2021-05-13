import copy

num_people, num_party = map(int, input().split())

truth_people = list(map(int, input().split()))[1:]
truth_people = set(truth_people)

party_members = []
for i in range(num_party):
    members = list(map(int, input().split()))[1:]
    party_members += [set(members)]

ans = num_party

for _ in range(num_party):
    for members in party_members:
        if members.intersection(truth_people):
            truth_people = truth_people.union(members)
for members in party_members:
    if members.intersection(truth_people):
        truth_people = truth_people.union(members)
        ans -= 1
print(ans)
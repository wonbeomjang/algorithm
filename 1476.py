date = {}

earth = 0
sun = 0
moon = 0

for i in range(15 * 28 * 19):
    date[f"{earth}_{sun}_{moon}"] = i
    earth = (earth + 1) % 15
    sun = (sun + 1) % 28
    moon = (moon + 1) % 19
    

earth, sun, moon = list(map(int, input().split(' ')))

print(date[f"{earth - 1}_{sun - 1}_{moon - 1}"] + 1)

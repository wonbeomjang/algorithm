import math

cross, heightR, widthR = map(int, input().split())

crossR = math.sqrt(heightR ** 2 + widthR ** 2)

R = cross / crossR

height = heightR * R
width = widthR * R

print(f"{int(height)} {int(width)}")
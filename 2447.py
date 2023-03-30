a=input()
b=input()
d=[[0]*(len(b)+1)for i in range(len(a)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        d[i+1][j+1]=d[i][j]+1if a[i]==b[j]else max(d[i][j+1],d[i+1][j])
print(d[-1][-1])
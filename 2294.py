n,k=map(int,input().split())
d=[0]+[1e5]*k
for c in(int(input())for i in range(n)):
 for i in range(c,k+1):d[i]=min(d[i],d[i-c]+1)
print(-1if d[-1]==1e5else d[-1])
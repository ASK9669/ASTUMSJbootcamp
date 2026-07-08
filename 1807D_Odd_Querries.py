t=int(input())
for i in range(t):
    n,q=map(int,input().split())
    c=list(map(int,input().split()))
    li=[0]*(n+1)
    for x in range(n):
        li[x+1]=c[x]+li[x]
    m=li[-1]
    for j in range(q):
        l,r,k=map(int,input().split())
        p=li[r]-li[l-1]
        le=r-l+1
        su=(m-p)+le*k
        if su%2!=0:
            print("YES")
        else:
            print("NO")

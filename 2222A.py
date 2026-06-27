x = int(input())
for i in range(x):
    b=int(input())
    arr=list(map(int,input().split()))
    if max(arr)==100:
        print("Yes")
    else:
        print("No")

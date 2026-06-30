t = int(input())
for j in range(t):
    n = int(input()) 
    s = map(int,input().split())
    arr = sorted(s)
    r = len(arr)-1
    b = 0
    red = arr[r]
    blue = arr[b] + arr[b+1]
    r = r-1
    b = b+2
    while b < r:
        red += arr[r]
        blue += arr[b]
        b += 1
        r -= 1
    if red > blue:
        print("YES")
    else:
        print("NO")

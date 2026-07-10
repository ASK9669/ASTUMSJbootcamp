t = int(input())

for i in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if p[i] <= i + 1:   # i+1 because indexing is 1-based
            ans += 1

    print(ans)

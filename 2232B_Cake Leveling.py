t = int(input())

for t in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pref = 0
    mn = float('inf')
    ans = []

    for i in range(n):
        pref += a[i]
        mn = min(mn, pref // (i + 1))
        ans.append(str(mn))

    print(" ".join(ans))

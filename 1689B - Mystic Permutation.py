t = int(input())

for j in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue

    unused = list(range(1, n + 1))
    ans = []

    for i in range(n):
        if len(unused) == 1:
            ans.append(unused.pop())
        else:
            if unused[0] != p[i]:
                ans.append(unused.pop(0))
            else:
                ans.append(unused.pop(1))

    if ans[-1] == p[-1]:
        ans[-1], ans[-2] = ans[-2], ans[-1]

    print(*ans)

# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))

#     ans = [-1] * n
#     seen = set()
#     pos = 0

#     for x in arr:
#         if x not in seen:
#             seen.add(x)
#             if pos < n:
#                 ans[pos] = x
#                 pos += 1

#     print(*ans)

t = int(input())
for t in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    seen = set()
    k = 0
    for time, post in enumerate(p, start=1):
        if post not in seen:
            seen.add(post)
            k += 1
            if k <= n:
                ans[n - k] = time

    print(*ans)

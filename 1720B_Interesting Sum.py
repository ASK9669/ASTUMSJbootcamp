t = int(input())

for t in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    print(a[-1] + a[-2] - a[0] - a[1])

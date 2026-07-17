t = int(input())

for t in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    seen = set()
    first = []
    extra = []

    for x in sorted(a):
        if x not in seen:
            seen.add(x)
            first.append(x)
        else:
            extra.append(x)

    print(*(first + extra))

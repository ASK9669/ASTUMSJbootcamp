from bisect import bisect_left

n, m = map(int, input().split())
a = list(map(int, input().split()))

prefix = []
total = 0

for x in a:
    total += x
    prefix.append(total)

for _ in range(m):
    b = int(input())

    i = bisect_left(prefix, b)

    previous = 0 if i == 0 else prefix[i - 1]

    print(i + 1, b - previous)

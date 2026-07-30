n, q = map(int, input().split())

prices = list(map(int, input().split()))
prices.sort()

prefix = [0]
for p in prices:
    prefix.append(prefix[-1] + p)

for _ in range(q):
    x, y = map(int, input().split())
    print(prefix[n - x + y] - prefix[n - x])

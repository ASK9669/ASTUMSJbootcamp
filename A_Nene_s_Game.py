t = int(input())

for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))

    x = a[0]

    queries = list(map(int, input().split()))

    for n in queries:
        print(min(n, x - 1), end=" ")
    print()

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = [0] * n
    i = 0

    while i < n:
        j = i

        # Find the group of equal sizes
        while j < n and a[j] == a[i]:
            j += 1

        # Only one shoe of this size -> impossible
        if j - i == 1:
            print(-1)
            break

        # Rotate indices
        for k in range(i, j):
            ans[k] = k + 2 if k + 1 < j else i + 1

        i = j

    else:
        print(*ans)  

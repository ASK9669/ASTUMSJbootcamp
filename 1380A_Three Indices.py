t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    left = [0] * n
    mn = 0
    left[0] = 0
    for i in range(1, n):
        if a[i] < a[mn]:
            mn = i
        left[i] = mn

    right = [0] * n
    mn = n - 1
    right[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        if a[i] < a[mn]:
            mn = i
        right[i] = mn

    ok = False
    for j in range(1, n - 1):
        i = left[j - 1]
        k = right[j + 1]
        if a[i] < a[j] and a[k] < a[j]:
            print("YES")
            print(i + 1, j + 1, k + 1)
            ok = True
            break

    if not ok:
        print("NO")

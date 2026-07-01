t = int(input())

for i in range(t):
    a, b, k = map(int, input().split())

    A = sorted(input())
    B = sorted(input())

    i = 0
    j = 0
    ca = 0
    cb = 0
    ans = ""

    while i < a and j < b:
        if (A[i] < B[j] and ca < k) or cb == k:
            ans += A[i]
            i += 1
            ca += 1
            cb = 0
        else:
            ans += B[j]
            j += 1
            cb += 1
            ca = 0

    print(ans)

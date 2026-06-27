t = int(input())

for j in range(t):
    n = int(input())
    s = input()

    ans = 0
    last = s[-1]

    for i in range(n - 1):
        if s[i] != last:
            ans += 1

    print(ans)

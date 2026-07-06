t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    diff = []

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            diff.append(i)

    ok = True
    for i in range(1, len(diff)):
        if diff[i] != diff[i - 1] + 1:
            ok = False
            break

    if ok:
        print("Yes")
    else:
        print("No")

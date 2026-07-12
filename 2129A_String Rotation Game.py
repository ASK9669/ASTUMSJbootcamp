t = int(input())

for j in range(t):
    n = int(input())
    s = input()

    blocks = 1
    a = False

    for i in range(1, n):
        if s[i] != s[i - 1]:
            blocks += 1
        else:
            a = True

    if not a or s[0] == s[-1]:
        print(blocks)
    else:
        print(blocks + 1)

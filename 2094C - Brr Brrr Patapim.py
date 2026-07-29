
for t in range(int(input())):
    n = int(input())

    total_arr = []
    ans = [0] * (2 * n + 1)

    for i in range(n):
        arr = list(map(int, input().split()))
        total_arr.extend(arr)

    for i in range(len(total_arr)):
        x = i % n + 1
        y = i // n + 1

        if x + y <= 2 * n:
            ans[x + y] = total_arr[i]

    seen = set(ans[2:])   # Ignore ans[0] and ans[1]

    for i in range(1, 2 * n + 1):
        if i not in seen:
            ans[1] = i
            break

    print(*ans[1:])

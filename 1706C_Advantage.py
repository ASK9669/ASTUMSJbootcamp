# t = int(input())
# for t in range(t):
#     n = int(input())
#     s = list(map(int, input().split()))
#     for num in s:
#         mx = max(s)
#         if num == mx:
#             y =sorted(s)
#             mx = y[-2]

#             print(num - mx, end=" ")
#         else:
#             print(num - mx, end=" ")
#     print()

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    y = sorted(s)
    mx = y[-1]
    second = y[-2]
    cnt = s.count(mx)

    for num in s:
        if num == mx and cnt == 1:
            print(num - second, end=" ")
        else:
            print(num - mx, end=" ")
    print()

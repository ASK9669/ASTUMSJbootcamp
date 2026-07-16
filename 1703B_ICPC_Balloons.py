t = int(input())
for i in range(t):
    n = int(input())
    
    s = input()
    arr = []
    c = 0
    for l in s:
        if l not in arr:
            c  += 2
            arr.append(l)
        else:
            c +=1
   

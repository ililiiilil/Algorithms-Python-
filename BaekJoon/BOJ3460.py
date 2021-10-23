t = int(input())

for _ in range(t):
    n = int(input())
    ans = []

    while n > 1:
        a = n % 2 
        n = n // 2  
        ans.append(a)
    
    if n == 1:
        ans.append(1)
    else:
        ans.append(0)
    
    for i in range(len(ans)):
        if ans[i] == 1:
            print(i, end= ' ')
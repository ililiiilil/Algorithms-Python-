t = int(input())

for _ in range(t):
    ans = list(input().split())
    res = float(ans.pop(0))

    for i in range(len(ans)):
        
        if ans[i] == '@':
            res *= 3
        elif ans[i] == '#':
            res -= 7
        elif ans[i] == '%':
            res += 5
    
    print("%0.2f" % res)
        

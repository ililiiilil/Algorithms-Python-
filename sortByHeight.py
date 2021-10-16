def sortByHeight(a):
    
    ans = []
    
    for i in range(len(a)):
        if a[i] != -1:
            ans.append(a[i])
            a[i] = 0
    
    ans.sort(reverse=True)
    
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = ans[-1]
            ans.pop()
    
    return a
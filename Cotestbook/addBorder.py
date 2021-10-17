def addBorder(picture):
    cnt = len(picture[0]) + 2
    
    ans = ['*' * cnt]
    
    for i in range(len(picture)):
        plus = '*' + picture[i] + '*'
        ans.append(plus)
    
    ans.append('*' * cnt)
    
    return ans
def solution(s):   
    ans = ''
    s = s.split(' ')

    for i in range(len(s)):
        if not s[i][0].isdecimal():
            s[i] = s[i][0].upper() + s[i][1:].lower()
        
        ans = ' '.join(s)
    
    return ans




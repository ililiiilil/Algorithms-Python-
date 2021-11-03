def solution(s):
    
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        
        elif i % 2 == 0:
            s[i].upper()

        else:
            s[i].lower()

    return s

print(solution('hi fsdjkfdn'))
        
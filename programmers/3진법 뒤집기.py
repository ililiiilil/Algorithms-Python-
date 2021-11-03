def solution(n):
    answer = 0
    s = [] 
    
    while True:
        if n == 0:
            break

        s.append(n % 3)
        n = n // 3 
    
    cnt = 0
    for i in range(len(s) - 1, -1, -1):
        answer += s[i] * (3 ** cnt)
        cnt += 1 
    
    return answer
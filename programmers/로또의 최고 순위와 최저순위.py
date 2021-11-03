def solution(lottos, win_nums):
    answer = []
    cnt = 0

    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    ans = cnt + 2
    if ans >= 6:
        ans = 6 

    if ans == 6:
        ans = 1
    elif ans == 5:
        ans = 2
    elif ans == 4:
        ans = 3 
    elif ans == 3:
        ans = 4
    elif ans == 2:
        ans = 5
    else:
        ans = 6
    
    if cnt == 6:
        cnt = 1
    elif cnt == 5:
        cnt = 2
    elif cnt == 4:
        cnt = 3 
    elif cnt == 3:
        cnt = 4
    elif cnt == 2:
        cnt = 5
    else:
        cnt = 6
    
    answer = [ans, cnt]

    return answer
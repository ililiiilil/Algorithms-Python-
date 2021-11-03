def solution(sizes):
    
    ans1 = []
    ans2 = []

    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            ans1.append(sizes[i][0])
            ans2.append(sizes[i][1])
        else:
            ans2.append(sizes[i][0])
            ans1.append(sizes[i][1])
    
    return max(ans1) * max(ans2)


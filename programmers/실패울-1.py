def solution(N, stages):
    result = {}
    denominator = len(stages)

    # denominator 라는 변수를 통해서 전체 인원의 크기를 알아보는거임.
    
    for stage in range(1, N + 1):
        if denominator != 0:
            count = stages.count(stage)
            result[stages] = count / denominator
            denominator -= count 
        
        else:
            result[stage] = 0
    
    # 전체 인원의 수가 '0'이 아닐때 / 내가 이 부분을 간과한거같다.
    # 그 스테이지만큼밖에 못온 인원을 차출해서 count에 넣고
    # 실패율을 계산한 이후에
    # 전체 인원을 다시 계산해준다
    
    return sorted(result, key = lambda x : result[x], reverse = True)
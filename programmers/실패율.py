def solution(N, stages):
    answer = dict()

    stage = 1
    while True:
        if stage > N:
            break
        s, f = 0, 0

        for i in range(len(stages)):
            if stages[i] != 0:
                if stages[i] > stage:
                    s += 1 
                else:
                    f += 1
                    stages[i] = 0
        
        answer[stage] = f / (s + f)
        stage += 1 

    answer = sorted(answer.items(), key = lambda x : x[1], reverse=True)        
    ans = []

    for i in answer:
        ans.append(i[0])

    return ans

#런타임 에러가 나오는부분이 많음.. 딕셔너리 쓰는 다른 사람 풀이를 참조해보려 함
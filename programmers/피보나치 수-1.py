def solution(n):
    ans = [1, 1]

    for i in range(2, n):
        ans.append(ans[i -1] + ans[i - 2])
    
    return ans[n - 1] % 1234567
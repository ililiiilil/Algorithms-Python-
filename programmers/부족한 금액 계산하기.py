def solution(price, money, count): 

    ans = 0 
    for i in range(1, count + 1):
        ans += price *i 

    if (ans - money) <= 0:
        return 0
    else:
        return ans - money    

   
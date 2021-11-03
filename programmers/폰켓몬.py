def solution(nums):
    
    N = len(nums)
    N /= 2 

    nums = list(set(nums))
    
    if N >= len(nums):
        return len(nums)
    else:
        return N
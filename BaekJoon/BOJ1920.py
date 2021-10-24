import sys

def quick_sort(arr, start, end):
    if start >= end:
        return 
    
    pivot = start
    left = start + 1 
    right = end 

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1 
        while right > start and arr[right] > arr[pivot]:
            right -= 1 
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

def binary_search(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    
    if arr[mid] == target:
        return 1 
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)
        
n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
quick_sort(arr1, 0, len(arr1) - 1)

m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

for i in arr2:
    print(binary_search(arr1, i, 0, len(arr1) - 1))

#quick sort와 이분탐색의 조합..



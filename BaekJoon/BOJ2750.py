n = int(input())
ans = []

for _ in range(n):
    ans.append(int(input()))

for i in range(len(ans) - 1):
    min_index = i
    for j in range(i + 1, len(ans)):
        if ans[min_index] > ans[j]:
            min_index = j 
    
    ans[i], ans[min_index] = ans[min_index], ans[i]
    
for i in ans:
    print(i)

#선택정렬
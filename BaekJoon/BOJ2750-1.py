n = int(input())

ans = []
for _ in range(n):
    ans.append(int(input()))

for i in range(1, len(ans)):
    for j in range(i, 0, -1):
        if ans[j] < ans[j - 1]:
            ans[j], ans[j - 1] = ans[j - 1], ans[j]

for i in ans:
    print(i)

#삽입정렬
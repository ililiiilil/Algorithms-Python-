n = int(input())

ans = [0, 1, 1, 2]

for i in range(4, 46):
    ans.append(ans[i - 1] + ans[i - 2])

print(ans[n])
t = 0
ans = []

for _ in range(10):
    a, b = map(int, input().split())
    t += b - a 
    ans.append(t)

print(max(ans))
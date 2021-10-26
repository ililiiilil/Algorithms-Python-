arr = [[0] * 101 for i in range(101)]

n = int(input())
for i in range(n):
    a, b = map(int, input().split())

    for j in range(b, b + 10):
        for k in range(a, a + 10):
            arr[j][k] = 1 

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j]:
            cnt += 1
 
print(cnt)
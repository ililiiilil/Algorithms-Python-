n = int(input())

for i in range(n):
    x, y = 100, 100
    a, b = map(int, input().split())
    
    if a > b:
        y -= a
    elif a < b:
        x -= b
    
print(x)
print(y)
    
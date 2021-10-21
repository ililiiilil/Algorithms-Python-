a, b = map(int, input().split())
c = int(input())

c1 = c // 60
c2 = c % 60 

a += c1
b += c2 

if b >= 60:
    b -= 60
    a += 1 

if a >= 24:
    a -= 24 

print(a, b)
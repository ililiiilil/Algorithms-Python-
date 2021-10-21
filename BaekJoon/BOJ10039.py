ans = []
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    ans.append(a)

print( int(sum(ans) / 5))
n = list(input())

a = len(n) // 10 
if a == 0:
    print(''.join(n))
else:
    for i in range(a):
        print(''.join(n[10 * i:10 * (i + 1)]))
    print(''.join(n[10 * (i + 1):]))
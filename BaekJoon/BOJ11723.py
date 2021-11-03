m = int(input())

def a(s, x):
    if x not in s:
        s.append(x)

def r(s, x):
    if x in s:
        s.remove(x)

def c(s, x):
    if x in s:
        print(1)
    else:
        print(0)

def t(s, x):
    if x in s:
        s.remove(x)
    else:
        s.append(x)

def all(s, x):
    s = [int(i) for i in range(1, 21)]

def empty():
    s = []

s = []
for i in range(m):
    ans = list(map(str, input().split()))
    if ans[0] == 'add':
        a(s, int(ans[1]))

    elif ans[0] == 'remove':
        r(s, int(ans[1]))
    
    elif ans[0] == 'check':
        r(s, int(ans[1]))
def push(ans, x):
    ans.append(x)
    return 

def pop(ans):
    if len(ans) == 0:
        print(-1)
    else:
        print(ans[-1])
        ans = ans[:-2]
    return

def size(ans):
    print(len(ans))
    return

def empty(ans):
    if len(ans) == 0:
        print(1)
    else:
        print(0)
    return

def top(ans):
    if len(ans) == 0:
        print(-1)
    else:
        print(ans[-1])
    return

n = int(input())
ans = []

for i in range(n):
    ans.append(input().split(" "))
    
    if ans[0] == 'push':
        push(ans, ans[1])
    elif ans[0] == 'pop':
        pop(ans)
    elif ans[0] == 'size':
        size(ans)
    elif ans[0] == 'empty':
        empty(ans)
    elif ans[0] == 'top':
        top(ans)
    
def gcd(a, b):
    while(b != 0):
        r = a % b 
        a, b = b, r 
    return a 

def lcd(a, b):
    return a * b / gcd(a, b)

a, b = map(int, input().split())

print(int(lcd(a, b)))


h, m, s = map(int, input().split())
ans = (h * 3600 + m * 60 + s + int(input()))
print((ans // 3600) % 24, (ans % 3600) // 60, ans % 60)
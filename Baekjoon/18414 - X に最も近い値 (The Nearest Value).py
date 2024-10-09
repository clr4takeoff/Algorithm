#B4_18414_X に最も近い値 (The Nearest Value)

x,l,r = map(int, input().split())
res = min(range(l, r+1), key=lambda i: abs(x-i))
print(res)

#S5_1769_3의 배수

x=input()
cnt=0

def digit_sum(n):
    return sum(int(digit) for digit in n)

while len(x)>1:
    x=str(digit_sum(x))
    cnt+=1

print(cnt)
print("YES" if int(x) % 3 == 0 else "NO")

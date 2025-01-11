#B3_2991_VAUVAU

a,b,c,d=map(int,input().split())
p,m,n=map(int,input().split())
def attack(t,a,b):
    return 1 if t%(a+b)<=a and t%(a+b)!=0 else 0
print(attack(p,a,b)+attack(p,c,d))
print(attack(m,a,b)+attack(m,c,d))
print(attack(n,a,b)+attack(n,c,d))

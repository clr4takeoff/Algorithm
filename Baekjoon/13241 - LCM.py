#S5_13241_LCM

import math
a,b=map(int,input().split())
gcd=math.gcd(a,b)
print(abs(a*b)//gcd)

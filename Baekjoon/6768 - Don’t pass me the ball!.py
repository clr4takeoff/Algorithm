#B3_6768_Don’t pass me the ball!

import math

j=int(input())

if j<4:
  print(0)
else:
  result = math.comb(j-1,3)
  print(result)

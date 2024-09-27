#S5_9512_Languages

import re

lng=[]
for _ in range(int(input())):
  d=input().split()
  lng.append([d[0]] + [word.lower() for word in d[1:]])

while True:
  try:
    a=input()
    test=list(re.split('[ ,.!?]',a.lower()))

    for i in lng:
      for j in range(len(test)):
        if test[j] in i[1:]:
          print(i[0])
          break

  except EOFError:
    break

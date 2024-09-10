#G2_1918_후위 표기식

from collections import deque

def postfix(a):
  st=[]
  li={"(":1, "+":2, "-":2, "/":3, "*":3}

  for i in a:
    if i.isalnum():
      print(i,end="")

    elif i=="(":
      st.append(i)

    elif i==")":
      while st and st[-1]!="(":
        print(st.pop(),end="")
      st.pop()

    else:
      while st and li[i]<=li[st[-1]] and st[-1] != "(":
        print(st.pop(),end="")
      st.append(i)
    
  while st:
    print(st.pop(),end="")

a=list(input())
postfix(a)

#B3_2547_사탕 선생 고창영

import sys
input=sys.stdin.readline
def S():
 t=int(input())
 for _ in range(t):
  input();n=int(input());s=0
  for _ in range(n):s=(s+int(input()))%n
  print("YES"if s==0 else"NO")
S()

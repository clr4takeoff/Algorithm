#B1_24839_2의 보수

N=int(input())
cnt=0
binN=bin(N & 0xFFFFFFFF)[2:].zfill(32)
comN=bin(~N+1 & 0xFFFFFFFF)[2:].zfill(32)
for i in range(32):
  if comN[i]!=binN[i]:
    cnt+=1
print(cnt)

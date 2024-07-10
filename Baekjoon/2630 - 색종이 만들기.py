#S2_2630_색종이 만들기

def maker(p):
    li=[]
    cnt=[0,0]
    li.append(p)

    while li:
        curr=li.pop()
        first = curr[0][0]
        paper = all(first==curr[i][j] for i in range(len(curr)) for j in range(len(curr)))

        if paper:
            cnt[first]+=1
        else:
            n=len(curr)
            half=n//2

            li.append([row[:half] for row in curr[:half]])
            li.append([row[half:] for row in curr[:half]])
            li.append([row[:half] for row in curr[half:]])
            li.append([row[half:] for row in curr[half:]])

    return cnt

n=int(input())
p=[]

for _ in range(n):
    a=list(map(int,input().split()))
    p.append(a)

result=maker(p)

print(result[0])
print(result[1])
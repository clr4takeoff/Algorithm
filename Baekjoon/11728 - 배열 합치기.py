#S5_11728_배열 합치기

n,m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

arr=a+b
arr.sort()

for i in range(len(arr)):
    print(arr[i], end=" ")

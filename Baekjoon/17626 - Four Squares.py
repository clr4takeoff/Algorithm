#S3_17626_Four Squares

import math

def is_square(n):
    return int(math.sqrt(n))**2==n

def find(n):
    if is_square(n):
        return 1

    for i in range(1,int(math.sqrt(n))+1):
        if is_square(n-i*i):
            return 2
    
    for i in range(1, int(math.sqrt(n))+1):
        for j in range(1, int(math.sqrt(n-i*i))+1):
            if is_square(n-i*i-j*j):
                return 3

    return 4

n=int(input())
print(find(n))
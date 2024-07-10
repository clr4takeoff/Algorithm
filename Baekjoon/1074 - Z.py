#S1_1074_Z

def Z(N,r,c):
    res=0
    size=2**N 

    while size>1:
        half=size//2
        
        if r<half and c<half:
            pass
        elif r<half and c>=half:
            res+= half*half
            c-=half
        elif r>=half and c<half:
            res+=2*half*half
            r-=half
        else:
            res+=3*half*half
            r-=half
            c-=half
        
        size=half

    return res

N,r,c=map(int,input().split())
print(Z(N,r,c))
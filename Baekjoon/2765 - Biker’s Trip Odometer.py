#B3_2765_Biker’s Trip Odometer

import sys
from math import pi
trip=1
while True:
    try:
        d,r,t=map(float,input().split())
        if r==0:break
        c=pi*d/12/5280
        dist=c*r
        mph=dist/(t/3600)
        print(f"Trip #{trip}: {dist:.2f} {mph:.2f}")
        trip+=1
    except:break

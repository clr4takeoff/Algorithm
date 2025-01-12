#B2_1408_24

from datetime import datetime, timedelta

c=input()
s=input()

c_t=datetime.strptime(c,"%H:%M:%S")
s_t=datetime.strptime(s,"%H:%M:%S")

if s_t<c_t:
    s_t+=timedelta(days=1)

r=s_t-c_t
print(str(r).zfill(8))

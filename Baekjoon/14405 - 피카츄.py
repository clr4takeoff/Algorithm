#S5_14405_피카츄

import re

def pikachu(s):
    pattern=re.compile(r'(pi|ka|chu)')
    s=pattern.sub('',s)
    
    if len(s)==0:
        return "YES"
    else:
        return "NO"

s=input().strip()

print(pikachu(s))

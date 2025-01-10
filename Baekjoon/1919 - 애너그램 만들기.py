#B2_1919_애너그램 만들기

a,b=input(),input()
from collections import Counter
c1,c2=Counter(a),Counter(b)
print(sum((c1-c2).values())+sum((c2-c1).values()))

#S5_1439_뒤집기

import re

s=input()
print(min(len(re.findall(r'1+',s)),len(re.findall(r'0+',s))))

import sys
import re
n = len(sys.argv)
strs=""
strs=sys.argv[1]
x =  re.sub(r"(?<=[\w+ ?])([A-Z])", r" \1", strs)
for c in x:
    if c.isupper():
        x = " "+x
        break
        
print(x.lower())
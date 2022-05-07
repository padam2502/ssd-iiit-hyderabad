import sys
n = len(sys.argv)
strs=""
strs=sys.argv[1]
x=""
lists=[]
dot=0
for i in range(int(len(strs))):
    if strs[i]!=" ":
        x+=strs[i]
        if strs[i]==".":
            dot=1
    else:
        if(x!=""):
            if dot==1:
                lists.append(float(x))
                dot=0
            else:
                lists.append(int(x))
            # print(x)
            x=""
if(x!=""):
    if dot==1:
        lists.append(float(x))
        dot=0
    else:
        lists.append(int(x))
lists.sort(key=lambda x:x)
# print(data)
print(lists)
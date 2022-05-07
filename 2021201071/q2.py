import sys
n = len(sys.argv)
binary=""
for i in range(1, n):
    binary+=(sys.argv[i])
if binary=="":
    print("TRUE")
else:
    
    decimal = 0
    decimal=int(binary, 2)
    strings=str(decimal)
    l=int(len(strings)/2)
    f=1
    for i in range(0,l):
            if strings[i] != strings[len(strings)-i-1]:
                f=0
                break
    if f==0:
        print("FALSE")
    else:
        print("TRUE")
        
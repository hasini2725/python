a=16
b=10
c=15
if(a>b and a>c):
    if(b>c):
        print(a,b,c)
    else:
        print(a,c,b)
elif(b>c and b>a):
    if(c>a):
        print(b,c,a)
    else:
        print(b,a,c)
elif(a>b):
    print(c,a,b)
else:
    print(c,b,a)

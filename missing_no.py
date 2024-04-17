a=[5,3,2,1]

def missing(a):
    if a[0]>a[1]:
        x=a[0]-a[1]
        y=a[1]-a[2]
        z=a[2]-a[3]
        b=0
    elif a[0]<a[1]:
        x=a[1]-a[0]
        y=a[2]-a[1]
        z=a[3]-a[2]
        b=1
    if (x==y):
        c=x
    elif(y==z):
        c=y
    elif(x==z):
        c=x
    if (b==1):
        for i in range(len(a)-1):
           if (a[i]+c!=a[i+1]):
            return (a[i]+c)
    if (b==0):
        for i in range(len(a)-1):
           if (a[i]-c!=a[i+1]):
            return (a[i]-c)


print(missing(a))

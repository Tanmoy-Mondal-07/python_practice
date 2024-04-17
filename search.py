a=[0,1,2,3,4,5,6,7,8,10]
b=int(input("enter a no"))
lo=0
hi=len(a)-1

def liner(a,b):
    for i in range(len(a)-1):
        if (b==a[i]):
            return(i+1)

def binary(a,b,hi,lo):
    m=hi+lo//2
    if (a[m]==b):
        return(m+1)
    elif (a[m]>=b):
        return(binary(a,b,m-1,lo))
    elif (a[m]<b):
        return(binary(a,b,hi,m+1))

print("the no l p.s",liner(a,b))

print("the no b p.s",binary(a,b,hi,lo))
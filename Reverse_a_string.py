a=[1,2,3,4,5]
c=0
x=a[::-1]
print(x)

b=len(a)-1
def rv(a,b,c):
    for i in range(c,b):
        a[i],a[b]=a[b],a[i]
        b=b-1
        c=c+1
        return(rv(a,b,c))
    return(a)
print (rv(a,b,c))
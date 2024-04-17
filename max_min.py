a=[23,114,46,2143,856,873,578304,10,153]
b=[a[0],a[len(a)-1]]

print(min(a))

def min_max(a,b):
    
    for i in range(0,len(a)-1):
        if(a[i]>=b[1]):
            b[1]=a[i]
        if(a[i]<=b[0]):
            b[0]=a[i]
    return(b)
b=(min_max(a,b))
print("min val=",b[0] ,"\nmax val=",b[1])
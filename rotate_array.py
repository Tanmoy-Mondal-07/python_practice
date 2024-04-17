a=[1,2,3,4,5]
b=2

def rotate(a,b):
    c=a[b:]+a[:b]
    return(c)

print(rotate(a,b))
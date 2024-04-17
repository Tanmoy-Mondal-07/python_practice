a=[1,1,2,3,4,5,5,5,5,5,6,7,8,8,8,8]
b=list(dict.fromkeys(a))

def fr(a,b):
    x=[]
    y=0
    for i in range(len(b)):
        for j in range(len(a)):
            if (b[i]==a[j]):
                y=y+1
                continue
        x.append(y)
        y=0
    return(x)

print(b,'\n',fr(a,b))
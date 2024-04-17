a=[1,2,3,4,5,6,7,8,8,8,8]
a=list(dict.fromkeys(a))
b=[2,8,9,10,8]
b=list(dict.fromkeys(b))
c=[]

def appd(a,b,c):
    for i in range(len(b)):
        for j in range(len(a)):
            if (b[i]==a[j]):
                c.append(b[i])
                continue
    return(c)


print(appd(a,b,c))
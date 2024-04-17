a=[1,2,3,4,5,2,6,7,8,1,5]


x=list(dict.fromkeys(a))
print(x)

def pop(a):
    b=len(a)-1
    for i in range(b):
        for j in range(b):
            if (i!=j and a[i]==a[j]):
                a.pop(j)
                b=len(a)-1
                continue
    return(a)

print(pop(a))
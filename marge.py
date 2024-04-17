a=[1,2,3,4,5,6,7,8]
b=[5,6,7,8,9,10]

a=set(a)
b=set(b)

print(a|b)#union
print(a&b)#inter
print(a-b)
print(a^b)#compliment of inter
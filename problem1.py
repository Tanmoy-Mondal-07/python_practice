import sys
a=[]
b=[]
x=input('enter:')

for i in x:
    a.append(i)

for j in a:
    if ord(j)==40 or ord(j)==91 or ord(j)==123:
        b.append(j)
    elif j == ')' or j =='}' or j ==']':
        c=b.pop()
        if c == "(" and j ==")" or c == "{" and j =="}" or c == "[" and j =="]":
            continue
        else:
            print("so funny:)")
            sys.exit()

if len(b) >0:
    print("error:(")
else:
    print('fine;)')
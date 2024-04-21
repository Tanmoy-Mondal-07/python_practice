class node:
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return True if self.top is None else False
    def push(self,value):
        new_node = node(value)
        new_node.next = self.top
        self.top=new_node
    def travers(self):
        temp=self.top
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def peek(self):
        if(self.isempty()):
            return'empty'
        else:
            return self.top.data
    def pop(self):
        if(self.isempty()):
            return("stack is empty")
        else:
            a=self.top.data
            self.top = self.top.next
            return(a)
    def size(self):
        temp=self.top
        x=0
        while temp is not None:
            temp=temp.next
            x+=1
        return (x)

l=[[0,0,1,1],[0,0,1,0],[0,0,0,0],[0,0,1,0]]
def find_celeb(l):
    s=stack()
    for i in range(len(l)):
        s.push(i)
    while s.size()>=2:
        i=s.pop()
        j=s.pop()
        if l[i][j]==0:
            s.push(i)
        else:
            s.push(j)
    celeb=s.pop()
    for i in range(len(l)):
        if i!=celeb:
            if l[i][celeb] == 0 or l[celeb][i]==1:
                print("no one is a celebrity")
                return
    print("the celebrity is",celeb)

find_celeb(l)
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

    

s=stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.pop()
s.pop()

print(s.isempty())
s.travers()
print(s.peek())


def text_editor(text, pattern):
    u = stack()
    r = stack()

    for i in text:
        u.push(i)
    for i in pattern:
        if i == "u":
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)
    res = ""
    while not u.isempty():
        res = f"{u.pop()}{res}"
    print(res)

text_editor("ahcucsav", "uuruu")
import sys

class node:
    def __init__(self,value):
        self.data=value
        self.next= None

class linkedlist:
    def __init__(self):
        self.head=None
        self.n=0
    def __len__(self):
        return self.n
    def insert_head(self,value):
        new_node = node(value)
        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1
    def __str__(self):
        curr=self.head
        result=''
        while curr!=None:
            result=result+str(curr.data)+'->'
            curr=curr.next
        return result[:-2]
    def insert_tail(self,value):
        new_node=node(value)#creating a new node
        curr=self.head
        while curr.next!=None:#also can use next.next.next
            curr=curr.next
        curr.next=new_node
        self.n=self.n+1
    def middle(self,after,value):
        new_node=node(value)
        curr=self.head
        while curr.next!=None:
            if curr.data==after:
                break
            curr=curr.next
        if curr.next!=None:
            new_node.next=curr.next
            curr.next=new_node
            self.n=self.n+1
        else:
            print('item not found')
    def clear(self):
        self.head=None
        self.n=0
    def remove_head(self):
        self.head=self.head.next
        self.n=self.n-1
    def pop(self):
        curr=self.head
        while curr.next.next!=None:
            curr=curr.next
        curr.next=None
        self.n=self.n-1
    def remove(self,point):
        curr=self.head
        while curr.next!=None:
            if curr.next.data==point:
                break
            else:
                curr=curr.next
        if curr.next==None:
            print("not found")
        else:
            curr.next=curr.next.next
    def search(self,item):
        curr=self.head
        pos=0

        while curr!=None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos=pos+1
        return 'not found'
    def __getitem__(self,index):
        curr=self.head
        for i in range(0,index):
            curr=curr.next
        return(curr.data)
    def revers(self):
        curr=self.head
        prev=None
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
    def if_loop(self):
        curr=self.head
        i=0
        while curr is not None:
            if i>=self.n:
                a='it\'s a loop , immediate termination'
                sys.exit(a)
            else:
                curr=curr.next
                i=i+1
        return 'not a loop'
    def loop(self):
        self.head.next.next.next.next=self.head
    # find middle elemint
    def mid(self):
        curr=self.head
        m=self.n//2
        for i in range(0,m):
            curr=curr.next
        print(curr.data)

# ctrl j for terminal

l=linkedlist()
l.insert_head(1)
l.insert_head(3)
l.insert_head(4)
l.insert_tail(0)
l.middle(3,2)


class link2list:
    def __init__(self):
        self.head=None
        self.n=0
    def __len__(self):
        return self.n
    def insert_head(self,value):
        new_node = node(value)
        new_node.next=self.head
        self.head=new_node
        self.n=self.n+1
    def __str__(self):
        curr=self.head
        result=''
        while curr!=None:
            result=result+str(curr.data)+'->'
            curr=curr.next
        return result[:-2]

l2=link2list()
l2.insert_head(5)
l2.insert_head(6)
l2.insert_head(7)
l2.insert_head(8)

print(l2)

class marge:
    def __init__(self):
        self.head=None
        self.n=0
    def __len__(self):
        return self.n
    # def insert_head(self,l,l2):
    #     a = l.head
    #     b = l2.head
    #     while a is not None and b is not None:
    #         if a.data > b.data:
    #             self._insert_node(a.data)
    #             a = a.next
    #         else:
    #             self._insert_node(b.data)
    #             b = b.next
    #     while a is not None:
    #         self._insert_node(a.data)
    #         a = a.next
    #     while b is not None:
    #         self._insert_node(b.data)
    #         b = b.next

    # def _insert_node(self, data):
    #     new_node = node(data)
    #     new_node.next = self.head
    #     self.head = new_node
    #     self.n += 1
    def insert_head(self,l,l2):
        a = l.head
        b = l2.head
        while a is not None and b is not None:
            if a.data > b.data:
                new_node = node(a.data)
                new_node.next=self.head
                self.head=new_node
                self.n=self.n+1
                a=a.next
            else:
                new_node = node(b.data)
                new_node.next=self.head
                self.head=new_node
                self.n=self.n+1
                b=b.next
        while a is not None:
            new_node = node(a.data)
            new_node.next=self.head
            self.head=new_node
            self.n=self.n+1
            a=a.next
        while b is not None:
            new_node = node(b.data)
            new_node.next=self.head
            self.head=new_node
            self.n=self.n+1
            b=b.next
        
    def __str__(self):
        curr=self.head
        result=''
        while curr!=None:
            result=result+str(curr.data)+'->'
            curr=curr.next
        return result[:-2]
m=marge()
m.insert_head(l,l2)
print(m)


# l.mid()
# l.revers()
# l.remove(1)
# l.pop()
# l.remove_head()
# l.clear()

# print(l.search(2))
# print(l[0])

# l.loop()
print(l.if_loop())


print (l)
# print (len(l))

# a=node(1)
# b=node(2)
# c=node(3)

# a.next=b
# b.next=c

# print(c.next)
# x=(str(a.next))
# y=x[25:43]
# print(int(y,16))
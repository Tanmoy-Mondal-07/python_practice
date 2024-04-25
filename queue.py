class node:
    def __init__(self,value):
        self.data=(value)
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        new_node = node(value)
        if self.rear is None:
            self.rear=new_node
            self.front=self.rear
        else:
            self.rear.next=new_node
            self.rear=new_node

    def dequeue(self):
        if self.front==None:
            print("empty")
        else:
            self.front=self.front.next

    def travers(self):
        temp=self.front
        out=''
        while temp is not None:
            out=out+str(temp.data)+"->"
            temp=temp.next
        print(out[:-2])


l=queue()

l.enqueue(1)
l.enqueue(2)
l.enqueue(3)
l.enqueue(4)
l.dequeue()

l.travers()
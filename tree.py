class treenode:
    def __init__(self,data):
        self.data = data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_lavel(self):
        lavel=0
        p=self.parent
        while p:
            lavel +=1
            p=p.parent
        return lavel
    def print_tree(self):
        print(f"{"   "*(self.get_lavel())}|__{self.data}")
        for child in self.children:
            child.print_tree()

def build_product_tree():
    root=treenode("electronics")

    laptop=treenode("laptop")
    laptop.add_child(treenode("mac"))
    laptop.add_child(treenode("asus"))
    laptop.add_child(treenode("acer"))

    phone=treenode("phone")
    phone.add_child(treenode("moto"))
    phone.add_child(treenode("samsung"))
    phone.add_child(treenode("appel"))


    root.add_child(laptop)
    root.add_child(phone)
    return root


if __name__=="__main__":
    root = build_product_tree()
    root.print_tree()
    pass
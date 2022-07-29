class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

    
class LinkList:
    def __init__(self):
        self.head=None

    def print_LL(self):
        n=self.head
        if n is None:
            print("LinkList is Empty")
        
        else:
            while (n is not None):
                print(n.data)
                n=n.ref
            
linklist1=LinkList()
linklist1.print_LL()

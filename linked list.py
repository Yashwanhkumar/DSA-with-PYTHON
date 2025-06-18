class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def traverse(self):
        if self.head is None:
            print("List is empty")
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
    def insert_at_specific(self,position,data):
            nb=node(data)
            a=self.head
            for i in range(1,position-1):
                a=a.next
            nb.next=a.next
            a.next=nb



n1=node(10)
ll=linkedlist()
ll.head=n1
n2=node(30)
n1.next=n2
n3=node(10)
n2.next=n3
ll.insert_at_specific(1,44)
ll.traverse()
class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
class circularDoubly:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty() :
            n.next=n
            n.prev=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.start is not None:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        else:
            n.prev=n
            n.next=n
            self.start=n
    def print_all(self):
        temp=self.start.next
        print(self.start.item, end=' ')
        while temp != self.start:
            print(temp.item, end=' ')
            temp=temp.next
        
            

myList = circularDoubly()
myList.insert_at_start(50)
myList.insert_at_start(40)
myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.insert_at_last(60)
myList.insert_at_last(70)
myList.insert_at_last(80)
myList.insert_at_last(90)
myList.print_all()
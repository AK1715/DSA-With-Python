class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class circularDoubly:
    def __init__(self,start=None):
        self.start=start
    def insert_at_start(self,data):
        n=Node(None,data,None)
        if self.start is not None:
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
            self.start=n
        else:
            self.start=n
    def print_all(self):
        temp=self.start
        while temp.next != self.start:
            print(temp.item, end=' ')
            if temp == self.start.next:
                break
            temp=temp.next
        
            

myList = circularDoubly()
myList.insert_at_start(50)
myList.insert_at_start(40)
myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.print_all()
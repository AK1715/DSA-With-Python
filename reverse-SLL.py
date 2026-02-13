class Node:
    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp=temp.next
    def reverse_ssl(self):
        prev=None
        current=self.start
        while current != None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.start=prev
    def reverse_item(self,data):
        if data is not None:
            prev=None
            current=self.start
            while current != None:
                    next=current.next
                    current.next=prev
                    prev=current
                    if  current.item == data:
                        break
                    current=next
            self.start.next=next
            self.start=prev

myList = SLL()
myList.insert_at_start(60)
myList.insert_at_start(50)
myList.insert_at_start(40)
myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_at_start(10)
# myList.reverse_ssl()
myList.reverse_item(30)
myList.print_list()
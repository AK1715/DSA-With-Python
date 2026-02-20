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
    def insert_after(self,tempValue,data):
        n=Node(data)
        if tempValue is not None:
            if self.start is None:
                return print("bhai tera list empty hai")
            else:
                temp=self.start
                while temp.next != self.start:
                    if temp.item == tempValue:
                        n.next=temp.next
                        n.prev=temp.next.prev
                        temp.next.prev=n
                        temp.next=n
                    else:
                        if temp.next == self.start:
                            n.next=self.start
                            n.prev=self.start.prev
                            self.start.prev.next=n
                        else:
                            print("bhai tu jo value diya vo list me nai hai")
                    temp=temp.next
    def delete_first(self):
            if self.start.next == self.start:
                print("are bas kr bhai ek last node delete nai hoga")
            self.start.prev.next=self.start.next
            self.start.next.prev=self.start.prev
            self.start=self.start.next
    def print_all(self):
        if self.start is not None:
            temp=self.start.next
            print(self.start.item, end=' ')
            while temp != self.start:
                print(temp.item, end=' ')
                temp=temp.next
        
            

myList = circularDoubly()
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.insert_at_last(30)
myList.insert_at_last(40)
myList.insert_at_last(50)
myList.insert_at_last(60)
# myList.insert_after(10,15)
myList.delete_first()
myList.delete_first()
myList.delete_first()
myList.delete_first()
myList.delete_first()
myList.delete_first()

myList.print_all()
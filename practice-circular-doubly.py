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
        if tempValue is None:
            return print("bhaiya kuch value to dedo")
        if self.start is None:
            print("List empty hai bhai")
            return
        temp=self.start
        while True:
            if temp.item == tempValue:
                n.next=temp.next
                n.prev=temp.next
                temp.next.prev=n
                temp.next=n
                return
            temp=temp.next
            if temp == self.start:
                break
    def delete_first(self):
            if self.start.next == self.start:
                print("are bas kr bhai ek last node delete nai hoga")
            self.start.prev.next=self.start.next
            self.start.next.prev=self.start.prev
            self.start=self.start.next
    def delete_last(self):
        if self.start.next == self.start:
            print("last node is remaining")
        self.start.prev.prev.next=self.start
        self.start.prev=self.start.prev.prev
    def delete_item(self,tempValue):
        if self.start == None:
            return
        if tempValue is None:
            return
        temp=self.start
        while True:
            if temp.item == tempValue:
                if temp.next == self.start:
                    self.start=None
                elif temp == self.start:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                    self.start=temp.next
                else:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                return
            temp=temp.next
            if temp == self.start:
                break
        print("Value not present")
    def search(self,value):
        if self.start is None:
            return print("bhai list mai kuch nai hai")
        temp=self.start
        while True:
            if temp.item == value:
                return print("haa bhai value list mai present hai")   
            temp=temp.next
            if temp == self.start:
                break
        print("bhai ye value list me nai hai")
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
myList.insert_after(60,15)
myList.insert_after(15,5)
myList.insert_after(20,25)
myList.delete_first()
myList.search(25)
myList.print_all()
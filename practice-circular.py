class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class circular:
    def __init__(self,last=None):
        self.last=last
    def insert_at_start(self,data):
        n=Node(data)
        if self.last is None:
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.last is None:
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
    def search(self,data):
        temp=self.last.next
        while temp is not None:
            if temp.item == data:
                return True
            if temp == self.last:
                break
            temp=temp.next
    def insert_after(self,tempVal,data):
        if self.last.next is not None:
            temp=self.last.next
            n=Node(data)
            while temp is not None:
                if temp.item == tempVal:
                    n.next=self.last.next
                    self.last.next=n
                    self.last=n
                if temp == self.last:
                    break
                temp=temp.next
    def delete_first(self):
            if self.last is None:
                return
            self.last.next=self.last.next.next
    def print_all(self):
        temp = self.last.next
        while temp is not None:
            print(temp.item, end=' ')
            if temp == self.last:
                break
            temp=temp.next
        


myList = circular()
myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.insert_at_start(5)
myList.insert_at_last(40)
myList.insert_after(40,25)
myList.insert_at_start(2)
myList.insert_at_last(50)
myList.insert_after(50,60)
myList.delete_first()
myList.delete_first()
myList.insert_at_start(5)
myList.print_all()

# print("\nit's present in list") if myList.search(40) else print("\nNot present")
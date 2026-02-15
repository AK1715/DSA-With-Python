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
myList.print_all()
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class circular:
    def __init__(self,start=None):
        self.start=start
    def insert_at_start(self,data):
            n=Node(data,self.start)
            self.start=n
            temp=self.start
            while temp.next is not None:
                temp=temp.next
                if temp.next is None:
                    temp.next=self.start

    def print_all(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp=temp.next


myList = circular()
myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.print_all()
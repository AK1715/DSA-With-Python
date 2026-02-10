class Node:
    def __init__(self,pre=None,item=None,next=None):
        self.pre=pre
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start
    def insert_at_start(self,data):
        n=Node(data)
        if self.start is not None:
            self.start.pre=n
            n.next=self.start
        else:
            self.start=n
    def print_dll(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp=temp.next

myList = DLL()
myList.insert_at_start(10)
myList.print_dll()
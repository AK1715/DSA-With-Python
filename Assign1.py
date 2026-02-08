# SLL 

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

myList = SLL()
myList.insert_at_start(5)
myList.insert_at_start(10)
myList.print_list()
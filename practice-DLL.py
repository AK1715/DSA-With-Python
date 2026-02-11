class Node:
    def __init__(self,pre=None,item=None,next=None):
        self.pre=pre
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if self.start is not None:
            self.start.pre=n
        self.start=n
    def insert_at_last(self,data):
        n=Node(self.start,data,None)
        temp=self.start
        if self.start is not None:
            while temp.next is not None:
                temp=temp.next
            n.pre=temp.item
            temp.next=n
        else:
            return print("list is empty")
    def search(self,data):
        if self.start is not None:
            temp=self.start
            while temp.item is not None:
                if temp.item == data:
                    return temp.item
                temp=temp.next
    def insert_after(self,afterValue,data):
        n=Node(self.start.pre,data,self.start.next)
        if self.start is not None:
            temp=self.start
            while temp.next is not None:
                if temp.item == afterValue:
                    n.pre=temp.item
                    n.next=temp.next
                    temp.next=n
                temp=temp.next 
        else:
            print("list is empty")
    # def insert_after(self,temp,data):
    #     n=Node(self.start.pre,data,self.start.next)
    #     if temp is not None:
    #         n.pre=self.start.item
    #         n.next=self.start.next
    #         self.start.next=n
    #     else:
    #         print("Not Given Argue of after value")
    def print_dll(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp=temp.next

myList = DLL()
myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.insert_at_last(40)
myList.insert_at_last(50)
myList.insert_after(40,45)
myList.insert_after(10,15)
myList.insert_at_start(5)
# myList.insert_after(myList.search(10),15)
myList.print_dll()
print()

# print("data is present in DLL") if myList.search(15) else print("Not present")
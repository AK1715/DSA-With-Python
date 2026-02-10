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
    def insert_at_last(self,data):
        n=Node(data)
        temp=self.start
        if self.start is not None:
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
    def insert_after(self,findValue,data):
        temp=self.start
        n=Node(data)
        while temp is not None:
            if temp.item == findValue:
                    n.next=temp.next
                    temp.next=n
            temp=temp.next
    def delete_start(self):
        if self.start is not None:
            self.start=self.start.next
        else:
            print("List is empty")
    def delete_last(self):
        # if self.start == None:
        #     return print("List is Empty")
        # if self.start.next == None:
        #     self.start=None
        #     return
        # temp=self.start
        # next=temp.next
        # while next.next is not None:
        #     temp=temp.next
        #     next=next.next
        # temp.next = None
        if self.start == None:
            return print("List is empty")
        if self.start.next == None:
            return self.delete_start()
        while self.start.next is not None:
            self.start.next=None
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp=temp.next

myList = SLL()
# myList.insert_after(5,15)
myList.insert_at_last(20)
myList.insert_at_start(10)
myList.insert_at_start(5)
myList.delete_start()
myList.delete_last()
myList.delete_last()
myList.delete_last()
myList.print_list()


# print("\nthis value is exist in list") if myList.search(15)  else print("Not exist")
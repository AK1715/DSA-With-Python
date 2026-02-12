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
            self.start=n
    def search(self,data):
        if self.start is not None:
            temp=self.start
            while temp is not None:
                if temp.item == data:
                    return temp
                temp=temp.next
            return None
    def insert_after(self,afterValue,data):
        n=Node(self.start.pre,data,self.start.next)
        if afterValue is not None:
            temp=self.start
            if temp.next == None:
                temp.next=n
                return
            while temp.next is not None:
                if temp.item == afterValue:
                    n.pre=temp.item
                    n.next=temp.next
                    temp.next=n
                temp=temp.next 
        else:
            print("list is empty",end=" ")
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
    def delete_first(self):
        if self.start is not None:
            self.start.pre=None
            self.start=self.start.next
        else:
            return print("LL is empty",end=" ")
            
    def delete_last(self):
        temp=self.start
        if temp is None :
            return print("LL is empty",end=" ")
        if temp.next is None :
            return self.delete_first()
        while temp.next.next is not None:
            temp=temp.next
        
        temp.next = None
        # temp = None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            # if temp.item == data:
            #     self.start=temp.next
            #     self.start.pre=None
            #     return
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.pre=temp.pre
                    if temp.pre is not None:
                        temp.pre.next=temp.next
                    else:
                        self.start=temp.next
                    return
                temp=temp.next


myList = DLL()
myList.insert_at_start(30)
myList.insert_at_start(20)
myList.insert_at_start(10)
# myList.insert_at_last(40)
# myList.insert_at_last(50)
myList.delete_item(10)
myList.delete_item(20)
myList.delete_item(30)
# myList.insert_after(40,45)
# myList.insert_after(10,15)
# myList.insert_at_start(5)
# myList.delete_last()
# myList.delete_last()
# myList.delete_last()
# myList.delete_first()

# myList.insert_after(myList.search(10),15) // if you want to uncomment then also uncomment method 
myList.print_dll()
print()

# print("data is present in DLL") if myList.search(15) else print("Not present")
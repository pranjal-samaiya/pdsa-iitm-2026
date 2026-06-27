class Node:
    def __init__(self,v=None):
        self.value = v 
        self.next = None
        return
    def isempty(self):
        if self.value ==None:
            return(True)
        else:
            return(False)
    def append(self,v):
        if self.isempty():
            self.value = value
        elif self.next== None:
            self.next = Node(v)
        else:
            self.next.append(v)
        return
    def appendi(self,v):
        if self.isempty():
            self.value =value 
            return
        temp = self
    def insert(self.v):
        if self,isempty():
            self.value= v 
            return
        newnode = Node(v)
        while temp.next != None:
            temp = temp.next
            temp.next = Node(v)
            return
    def insert(self.v):
        if self,isempty():
            self.value= v 
            return
        newnode = Node(v)
        (self.value , newnode.next) = (newnode.value ,self.value)
        (self.next,newnode.next )= (newnode,self.next)
    def delete(self.v):
        if self.isempty()


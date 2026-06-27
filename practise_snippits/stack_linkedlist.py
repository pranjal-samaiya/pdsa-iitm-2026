# class Node:
#     def __init__ (self,data):
#         self.data = data
#         self.next = None
# class Stack :
#     def __init__ (self):
#         self.top = None
#     def isempty (self):
#         if self.top == None:
#             return True
#         else:
#             return False
#     def Push(self,data):
#         if self.isempty():
#             self.top = Node(data)
#         else:
#             temp = Node(data)
#             temp.next =self.top
#             self.top = temp 
#     def pop(self):
#         if self.isempty() == True:
#             return None
#         else:
#             temp =self.top.data
#             self.top =self.top.next
#             return temp
#     def display (self):
#             if self.isempty() ==True:
#                 return None
#             else:
#                 temp = self.top
#                 while temp != None:
#                     print(temp.data)
#                     temp = temp.next
class Node:
    def __init__ (self,data):
         self.data = data
         self.next = None
class Stack:
    def __init__ (self):
        self.top = None
    def isempty(self):
        if self.top ==None:
            return True 
        else : 
            return False
    def Push(self,data):
        if self.isempty == True:
            self.top = Node(data)
        else:
            newValue = Node(data)
            newValue.next = self.top
            self.top = newValue
    def Pop(self):
        if self.isempty==True:
            return None
        else:
            popper_value = self.top
            self.top = self.top.next
            return popper_value.data
    def Peek (self):
        if self.isempty ():
            return "stack is empty"
        return self.top
    def display(self):
        temp = self.top
        while temp != None :
            print(temp.data)
            temp = temp.next
    def __str__(self):
        return str(self.data)

S = Stack()
S.Push(30)
S.Push(40)
S.Push(50)
S.Push(60)
S.Push(70)
print(S.Pop())
print(S.Pop())
S.display()
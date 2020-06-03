## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}
print(type(l),type(s),type(d))

## 3. Defining a Class ##

class NewList():
    pass

## 4. Instantiating a Class ##

class NewList(DQ):
    pass
newlist_1=NewList()
print(type(newlist_1))

## 5. Creating Methods ##

class NewList(DQ):
    def first_method():
        return "This is my first method"
newlist=NewList()
print(newlist)

## 6. Understanding 'self' ##

class NewList(DQ):
    def first_method(self):
        return "This is my first method"
newlist=NewList()
result=newlist.first_method()
print(result)
print(newlist)
newlist.first_method()

## 7. Creating a Method That Accepts an Argument ##

class NewList(DQ):
    def return_list(self,input_list):
        return input_list
newlist=NewList()
result=newlist.return_list([1,2,3])
print(result)

## 8. Attributes and the Init Method ##

class NewList(DQ):
    def __init__(self,initial_state):
        self.data=initial_state
my_list=NewList([1,2,3,4,5])
print(my_list.data)

## 9. Creating an Append Method ##

class NewList(DQ):
    def __init__ (self, initial_state):
        self.data = initial_state
    def append(self,new_item):
        self.data=self.data+[new_item]
my_list=NewList([1,2,3,4,5])
my_list.append(6)
print(my_list.data)

## 10. Creating and Updating an Attribute ##

# The NewList definition from the previous
# screen is copied here for your convenience

class NewList(DQ):
#     """
#     A Python list with some extras!
#     """
    def __init__(self, initial_state):
        self.data = initial_state
        self.calc_length()
    def calc_length(self):    
        length=0
        for item in self.data:
            length+=1
        self.length=length    
    
    def append(self, new_item):
#         """
#         Append `new_item` to the NewList
#         """
        self.data = self.data + [new_item]
        self.calc_length()
fibonacci=NewList([1,1,2,3,5]) 
fibonacci.append(8)
print(fibonacci.length)
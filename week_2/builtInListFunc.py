#This program demonstrates various built-in list functions in Python.
#Creating empty list
List=[]
print(List)
#elements in list
List = ['python','Mathematics','chemistry', 1997, 2000]
print(List)
#inserting value into list using insert()
List.insert(2, 10087)
print(List)
#diplay length of list
print(len(List))
#remove an element from the list
List.remove(1997)
print(List)
#add element into the list at last using append()
List.append(20544)
print(List)
#delete an element using pop() returns deleted element
print(List.pop())
#clear the list
print(List.clear())
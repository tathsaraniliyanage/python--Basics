fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  print(type(x))
  
color = ["pink","yellow","white"]  
print(color)
print(type(color))
print(color[1])

# array ek reverse kirima
color.reverse()
print(color)

# array eke end ekata alutin element ekak add kirima
color.append("orange")
print(color)

# remove all elments from the list
color.clear()
print(color)

# returns a copy of the list
color = ["pink","yellow","white"] 
color.copy()
print(color)

# Returns the number of elements with the specified value
color.count(0)
print(color)

# Add the elements of a list (or any iterable), to the end of the current list
# color.extend(1)
# print(color)

# Returns the index of the first element with the specified value
print("index")
color.index(color[1])
print(color)

# Adds an element at the specified position
# color.insert("banana")
# print(color)

# Removes the element at the specified position
color.pop()
print(color)

# Sorts the list
color.sort()
print(color)

























# message = "hello"
# print(message  * 2)

#(membership opertors)
# in   not in :  
# # var = "hello Rayan"
# print("Ra" not in var)

# msg_1 = "hello"
# print(msg_1[0])
# print(len(msg_1))


# slicing and indexing    interning
# Assingment#1:  assci code     ,    binary decimal hexadecimal forms 

# Start of AI which greets with first name
# name = "Muhammad"
# greeting = "hello"
# print(greeting , name)

# String formation: 

# %s = string   %d = integer  %f = float %x =int is hexadecimal form 

# name = "Alice"
# age = 29
# Using % operator    (if format of age and name is changed in the brackets thenn we will get a error)
# print("my name is %s and my age is %d" % (name,age))

# Using format:
# print("my name is {} and my age is {}".format(name,age))/

# Using f-string :
# print(f"My name is {name} and my age is {age}")

# Escape sequences: 

# greetings = 'Rehan\'s greetings'
# print(greetings)

# result = "Rayan\
# hello"
# print(result)

# greetings = 'Rehan\'s \n greetings'
# print(greetings)

# type , dir and id functions:x
# 'type' : to find datatype 
# dir : to find all functions of that datatype
# id : to find memory address of that data
# name = "Ryan"
# print(type(name))
# print(f"dir is : {dir(name)}")
# print(f"id is :{id(name)}")

# Mutable and Immutable:
# name = "rehan"
# print(id(name))
# name = "Usman"
# print(id(name))

# name_list = ["Rehan","Ali"]
# print(id(name_list))

# name_list.append("Usman")
# print(id(name_list))



# Comments in python:
# name = "abc" # this is a single line comment

"""
This is 
a multi line 
comment
"""



# Advanced datatypes:
# 1.list:  # we can add any type of data in a list
# student_name = ["Ali","Usman","Rehan",45]
# print(student_name[len(student_name)-1])  #-1 is used for last element

# student_name.append("Haris") #append is used to add an element
# print(student_name)

# student_name.insert(1,"Haris") #insert is used to add an element at a specific index
# print(student_name)

# student_name.pop()
# print(student_name)

# del student_name[:2] #delete the first two elements from the list
# print(student_name)

# slice notation:
# [start:end:jump]
teacher_names = ["Rehan","Usman","Ibtisam","Sir Zia"]
senior_teachers = teacher_names[1:4:2]
print(senior_teachers)
#  matrix is a list in a list

# mat = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print(mat[0][2])  #To print "3"

# for row in mat:
#     for column in row:
#         print(column)


# def greet(name):
#     print(f"Hello {name}")

# greet("Ali")

# def add (a,b):
#     return(a+b)

# print(add(9,8))

# def multiply():
#     number_1 = int(input("Enter first number to multiply: "))
#     number_2 = int(input("Enter second number to multiply: "))    
#     return number_1 * number_2

# print(multiply())

# def calc(a,b,c):
#     result = a + b
#     return result*c

# print(calc(3,7,34))


# def info(name = "Uzair",age = 12):
#     print(f"Hello {name}! You are {age} years old")

# info(age = 14)

# def check_list(sample_list):
#     sample_list.append(4)
#     print(sample_list)

# sample_list = [1,2,3]
# check_list(sample_list)
# print(sample_list)


# def greetings(n):
#     global name
#     name = "Rehan"
#     print(f'Hello {name}')

# name = "Usman"
# greetings(name)
# print(f"Hello {name}")



# def factorial(n):
#     if n < 0:
#         return None
#     elif n < 2:
#         return 1
#     else:
#         result = 1
#         for i in range(2,n+1):
#             result *= i
#         return result

# print(factorial(5)) 

      #  Lambda function:

numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x:x**2, numbers))
print(squared_numbers)
# Tested with https://www.programiz.com/python-programming/online-compiler/

# Addition - given two inputs and then give the sum 
print("Give me two numbers to add")
a = int(input("Type a number: "))
b = int(input("Type another number: "))
print("The sum is ", a+b)

# Subtraction - given two inputs and then give the difference 
print("Give me two numbers to subtract")
a = int(input("Type a number: "))
b = int(input("Type another number: "))
print("The difference is ", a-b)


# Multiplication - given two inputs and then give the product 
print("Give me two numbers to multiply")
a = int(input("Type a number: "))
b = int(input("Type another number: "))
print("The product is ", a*b)


# Division - given two inputs and then give the factor 
try:
    a = int(input("Type a number: "))
    b = int(input("Type another number: "))
    result = a / b
    print("the factor is", a/b)
#Cant divide by zero! 
except ZeroDivisionError as e:
    print(e)

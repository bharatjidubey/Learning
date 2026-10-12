
# 1. Check try and Except
# text = input("Enter a whole number: ")
# try:
#     number = int(text)
#     print("Square:", number * number)
# except ValueError:
#     print("That is not a whole number.")


# With input abc, the output is That is not a whole number.; with input 4, it is Square: 16.


#----------------------------------------------------------------------------------------------------------------------

# 2. Show Major Errors

# print("ABC)                 #syntax error

# b = 3 / 0                   #Runtime error - zero division error
# print(b)

# l = int(input("Enter Size l : "))
# b = int(input("Enter Size b : "))
# area = l + b                               # logical error give answers wrong
# print("area : ", area)


#----------------------------------------------------------------------------------------------------------------------

# BMI Calculator

# BMI = W / h^2       - formula.

# w = float(input("Enter weight"))
# h = float(input("Enter hight in meters"))

# bmi = w / (h*h)
# print("BMI : " , bmi)


#----------------------------------------------------------------------------------------------------------------------

# Even & Odd

# for even x divide by 2 is 0 for odd its never zero

# x = float(input("Enter no."))

# if x % 2 == 0:
#     print("EVEN")
# else:
#     print("ODDI")


#-----------------------------------------------------------------------
# Guessing Game

# import random
# secret = random.randint(1,3)

# guess = int(input("Guess the no (1-21) : "))

# while guess != secret:
#     print("try")
#     guess = int(input("Guess the no (1-21) : "))
# print("Correct")


#------------------------------------------------------------------------

# Average of three no.s

# a+b+c / 2 simple

# a = float(input("Enter the no. : "))
# b = float(input("Enter the no. : "))
# c = float(input("Enter the no. : "))

# avg = (a+b+c) / 3
# print("average : ", avg)

#------------------------------------------------------------------------

# Swap two variables
a, b = 10, 20
temp = a               # with a temporary variable
a = b
b = temp
print(a, b)            # 20 10

a, b = 10, 20
a, b = b, a            # without a temporary variable
print(a, b)            # 20 10








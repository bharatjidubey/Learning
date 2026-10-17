
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

# # Swap two variables
# a, b = 10, 20
# temp = a               # with a temporary variable
# a = b
# b = temp
# print(a, b)            # 20 10

# a, b = 10, 20
# a, b = b, a            # without a temporary variable
# print(a, b)            # 20 10


#------------------------------------------------------------------------

# Leap Year

# if x % 400 == 0   mean confirm leap year.
# if x % 4 == 0 and x % 100 != 0  means confirm leap year.

# x = int(input("Enter year"))

# if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a leap year")


#------------------------------------------------------------------------

# Calculator using If - Else 


# x = int(input("Enter the no."))
# o = input("Enter the operator :  +  -  *  /  %  ** : ")
# y = int(input("Enter the no."))


# if o == "+":
#     print(x+y)
# if o == "-":
#     print(x-y)
# if o == "*":
#     print(x*y)
# if o == "/":
#     print(x/y)
# if o == "%":
#     print(x%y)
# if o == "**":
#     print(x**y)
# else:
#     print("Wrong input")


#--- or ---

# if o == "+":
#     print(x+y)
# elif o == "-":
#     print(x-y)
# elif o == "*":
#     print(x*y)
# elif o == "/":
#     print(x/y)
# elif o == "%":
#     print(x%y)
# elif o == "**":
#     print(x**y)
# else:
#     print("Wrong input")


#--- or ---


# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# print("5. Modulus")
# print("6. Power")

# operator = int(input("Enter the number for operation: "))
# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))

# match operator:
#     case 1:
#         print(x + y)
#     case 2:
#         print(x - y)
#     case 3:
#         print(x * y)
#     case 4:
#         print(x / y)
#     case 5:
#         print(x % y)
#     case 6:
#         print(x ** y)
#     case _:
#         print("Invalid operation")



#------------------------------------------------------------------------
# Simple & Compound Intrest

# SI = (P * R * T) / 100


# printciple = 1000  &  Rate = 10%  &  Time = 3y
# Year 1 interest = ₹100  //   Year 2 interest = ₹100  //   Year 3 interest = ₹100    ~~  Total interest = ₹300

# Total amount = ₹1,000 + ₹300 = ₹1,300

# #--- or ---

# F = P (1 + R/100)^T
# CI = F - P

# printciple = 1000  &  Rate = 10%  &  Time = 3y
# Year 1: ₹1,000 + ₹100 = ₹1,100  //  Year 2: ₹1,100 + ₹110 = ₹1,210  //  Year 3: ₹1,210 + ₹121 = ₹1,331

# Total amount = ₹1,000 + ₹331 = ₹1,331

# #--- or ---


# P = float(input("Enter the Amt. : "))
# R = float(input("Enter the Rate. : "))
# T = float(input("Enter the Time. : "))

# choice = int(input("Enter 1. - Simple Intreset // 2. - Compound Intrest // 3. - Both : "))
# print("---------------------")

# if choice == 1:
#     SI = (P * R * T) / 100
#     print("Simple Intreset : ", SI)
#     print("Total Amt. : ", P + SI)

# if choice == 2:
#     F =  P * ((1 + (R/100))**T)
#     CI = F - P

#     print("COmpound Intrest : ", CI)
#     print("Total Amt. : ", F)

# if choice == 3:
#     SI = (P * R * T) / 100
#     print(f"Simple Interest: {SI:.2f}")
#     print(f"Total Amount: {P + SI:.2f}")

#     print("---------------------")

#     F =  P * ((1 + (R/100))**T)
#     CI = F - P
#     print(f"Compound Interest: {CI:.2f}")
#     print(f"Total Amount: {F:.2f}")





# Celsius to Fahrenheit        //        Fahrenheit to Celsius
# F = (C * 9/5 ) + 32         //          C = (F - 32) * 5/9

# choice = int(input(" Enter : 1. - Celsius to Fahrenheit  //  2. - Fahrenheit to Celsius : "))

# if choice == 1:
#     C = int(input("Enter the degree : "))
#     F = (C * 9/5 ) + 32 
#     print(f"Fehrenheite : {F:.2f} °C")

# if choice == 2:
#     F = int(input("Enter the degree : "))
#     C = (F - 32) * 5/9
#     print(f"Celsius : {C:.2f} °C")


#------------------------------------------------------------------------

# Count digits, sum of digits and reverse a number


# x = 1234
# reverse = 0
# total = 0
# count = 0
# while x > 0:
#     digit = x % 10            
#     x //= 10
    
#     reverse = reverse * 10 + digit     # builds the reversed number

#     total += digit                     # sum of digits
#     count += 1                         # number of digits
    
# print(reverse, total, count)           # 4321 10 4


#------------------------------------------------------------------------

# Pallindrom - read forward = read backword  like 121 = 121

# n = int(input("Enter a number: "))
# temp = n
# reverse = 0

# while temp > 0:
#     x = temp % 10                      # as remainder % give last digit
#     temp = temp // 10                   #  as value it remove last digit bcaz it wont count decimal give whole no.
#     reverse = reverse * 10 + x

# if n == reverse:
#     print(n, "is a palindrome")
# else:
#     print(n, "is not a palindrome")



#------------------------------------------------------------------------


# Armstrong no. 

# 123 = 1^3   +   2^3     +   3^3     =   1 + 8 + 27 = 36

# here 1st count the no.of digit. then seprate the digits. then every digit have power as no.of digits.


# n = int(input("Enter the no.: "))

# temp = n
# count = len(str(n))
# sum = 0

# while temp > 0:
#     x = temp % 10
#     temp = temp // 10
#     sum = sum + x ** count

# if sum == n:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



# Factorial

# here, 5! = 5 * 4 * 3 * 2 * 1 = 120

# x = int(input("Enter the no."))
# temp = x
# fact = 1

# while temp:
#     fact = fact * temp
#     temp = temp - 1

# print(fact)

# -- or -- 

# def fact(x):
#     if x == 0 or x == 1:
#         return 1                #base case

#     if x > 0:
#         return x * fact(x-1)

# x = int(input("Enter the no."))
# print(fact(x))


#------------------------------------------------------------------------

# Prime no.

# x = int(input("Enter the no."))

# if x <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, x):                   # here we check 2 to n range bcs  btw that range is only possiblity to get whole no. and n + values give decimal.
#         if x % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")


#------------------------------------------------------------------------

# GCD and LCM
# GCD(a,b) = GCD(b, a%b)

# ex. 8 & 3 = (8%3) = (3%2) = (2%1) = (0) = GCD(1)

# LCM = (a * b) / GCD


# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))

# # Handle the special case
# if x == 0 and y == 0:
#     print("GCD and LCM are undefined for (0, 0)")
# else:
#     # Preserve original values
#     a, b = abs(x), abs(y)

#     while b != 0:
#         a, b = b, a % b

#     gcd = a

#     lcm = abs(x * y) // gcd

#     print("GCD:", gcd)
#     print("LCM:", lcm)





#  Fibonacci series
# Each term is the sum of the two before it, starting 0, 1, 1, 2, 3, 5, 8, 13.    

# len is n  &   itrations also n times.

# n = int(input("How many terms? "))
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
# print()


#------------------------------------------------------------------------

#Count positive, negative and zero values

# ls = [11,15,-15,21,18,5,-21,0]

# pos = neg = zero = 0

# for x in ls:
#     if x > 0:
#         pos += 1
#     elif x < 0:
#         neg += 1
#     else:
#         zero += 1

# print(pos,neg,zero)

# -- or -- 

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial(5))               # 120



#------------------------------------------------------------------------

# -------  function calling by __name__

#--file name - calc.py -- main file
# def add(a, b):
#     return a + b

# def main():
#     print("My Calculator")
#     print(add(10, 20))

# print("xyxx")

# we use if when -
# mean when i want to run function directly on main file, but it should not run directly on imported file.

# if __name__ == "__main__":                  # __name__  ye by deafult hai python mai, when file run name alredy stores main then we check (name == main) as we name stores main when we ri=un so main = main condn true. 
#     main()


# -- test.py -- 
# import calc
# print(calc.add(5, 3))
# print(calc.main())


#------------------------------------------------------------------------

# # Arguments by postional, keyword, default , arg & keword argument

# def add(a, b=2, *args):
#     return a + b + sum(args)

# print(add(1))               # 3     a=1, b=2
# print(add(1, 2, 3, 4))      # 10    a=1, b=2, args=(3, 4)

# def show(a, b=2, *args, **kwargs):              #args give tuple & kwargs give dictionary
#     return a, b, args, kwargs

# print(show(1, 3, 4, 5, x=9))   # (1, 3, (4, 5), {'x': 9})











# #python file save as .py 

#Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, but the standard indentation requires standard Python code to use four spaces.

#A computer program is a list of "instructions" to be "executed" by a computer.

#--------------------------------------------------------------------------------------------------------
# #Module - a file containing code of others.
# #we use "pip" to instal module. pip is pakage manager of python.
# #ex. - pip install pyjoke


# to work python on cmd / powershell -- write 'python' in terminal

# --------------------------------------------------------------------------------------------------------

# #pip install pyjokes  - in terminal
# import pyjokes

# joke = pyjokes.get_joke()
# print(joke)

#or

# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say(" fuck the python hard")
# engine.runAndWait()

# --------------------------------------------------------------------------------------------------------

# - comments - interpreter wont read these lines.
# use '#' or press 'ctrl + /'    - single line comment.
#  multiline comments use triple double / single qoute. """ xyz """

#--------------------------------------------------------------------------------------------------------

# print()    -  sends output to the screen.
# to print simple string - print(" xyz ")
# print(x, y, z)
# print(x + y + z)
# to print mutilines use triple single / double qoute - print(''' xyz ''')

# print(" xyz ")
# print(''' x
#     y
#         z ''')


#--------------------------------------------------------------------------------------------------------

# input() reads what the user types and always returns a string, even if the user types digits.
# name = input('Enter your name: ')

#vari_name = input("enter xyx : ")
#print(f"xyz,{vari_name}") - via f we can use variable at mid of string  or      print("xyz", vari_name)  

#--------------------------------------------------------------------------------------------------------

# variable - A container - it stores values like intereger string etc.
# variable name should be not any keyword, _aa , aa_aa , valids incliding numeric.
# variable name start with slphabate underscore but not numeric in mid underscore valid, and numic also valid in mid.

#x = y = z = "Orange"  //  x, y, z = "Orange", "Banana", "Cherry"


# CAsting - changing data tyoe. -----------------------------
# x = str(3)
# y = int(3)
# z = float(3)

#type() - it give data type
# print(type(x))

# --------------------------------------------------------------------------------------------------------

# Datatype
# integer
# Floating
# string
# boolean
# none

# Example                                        Data Type

# x = "Hello World"                              str
# x = 20                                         int
# x = 20.5                                       float
# x = 1j                                         complex
# x = ["apple", "banana", "cherry"]              list
# x = ("apple", "banana", "cherry")              tuple
# x = range(6)                                   range
# x = {"name": "John", "age": 36}                dict
# x = {"apple", "banana", "cherry"}              set
# x = frozenset({"apple", "banana", "cherry"})   frozenset
# x = True                                       bool
# x = b"Hello"                                   bytes
# x = bytearray(5)                               bytearray
# x = memoryview(bytes(5))                       memoryview
# x = None                                       NoneType

#--------------------------------------------------------------------------------------------------------

# operators & operands

# operands are variable and operators are = + - * etc

# 1. Assignment operator    :   =  +=  -=  *=  /=  %=
# 2. comperision operator   :   >  <  !=  >=  <=    ==      Relational
# 3. arithmatic operator    :   +  -  *  /  //  %  **
# 4. logical operators      :   and or not
# 5. Membership Operator    :   in, not in, is, is not

  


# a += 2    means a =  a + 2 = ...

#--------------------------------------------------------------------------------------------------------

#Strings - these are immutable orignal string not change, a new changed string should print.
#           - A string is a sequence of characters inside single, double or triple quotes.

# print(" xyz ")
# print(''' x
#     y
#         z ''')


#   looping     ------
# for x in "banana":
#   print(x)


# Check fxn - To check if a certain phrase or character is present in a string, we can use the keyword in.
# txt = "The best things in life are free!"
# print("free" in txt)                            # True   & using membership oprator 'in'

# txt = "The best things in life are free!"
# print("expensive" not in txt)


# if function - 
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")


#   Indexing    -----

# indexing in string    h e l l o     0 1 2 3 4 then -1 -2 -3 -4 -5     0, -5 both show h  &  4, -1 showes o
#last index in range not included.

# Slicing - to return a part of the string.

# b = "Hello, World!"
# print(vari_name[:8])                    here comma & space counted remember.
# print(vari_name[:8])  
# print(vari_name[-9:-1])	#o,world
# print(vari_name[:-9])  #Hell   2nd last l is -9 so range is like 0 -12 -11 -10 -9
# print(vari_name[-1:])  # probably we cant print ! on last in negative indexing, for print that 

#b = "abcdefghijklmnopqrst"
#print(b[0:9:2]) - b[start : stop : step]
#acegi


#   Methods -----

# b = "abcdefghijklmnopqrst"

#print(len("hello"))       or    print(len(b))      - count space

#print(b.lower())       or    print("xyz".upper()) 
#print(b.upper())       or    print("xyz".upper()) 
#print(b.capitalization())

#print(b.replace())
#print(b.replace("old", "new", 1))    or       #print(b.replace("old", "new", 1).replace("xx", "yy")) -  1 means only 1 time replace.

#print(b.find("xyz"))   - give index where it start else -1 not found

#print(b.strip())   or    print(vari_name.strip())    -  it remove space from both end not from mid.
#print(b.lstrip())    or    print(vari_name.lstrip())     -    it remove space from left end
#print(b.rstrip())    or    print(vari_name.rstrip())      -   it remove space from right end

#print(b.count("2"))   -   occurance

# print(b.split())        -       ['Hello', 'World']

# print("Python Programming".find("Program"))     -   it gives starting position
# print(b.find("World"))      -       it gives starting position

# print(vari_name.endswith("xyz"))       -    true / false
# print(vari_name.startswith("xyz"))       -        true / false
#print(vari_name.capitalswith("xyz"))


# b.isalpha()     # only letters?
# b.isdigit()     # only numbers?
# b.isalnum()     # letters + numbers?
# b.isspace()     # only spaces?
# b.islower()     # all lowercase?
# b.isupper()     # all uppercase?


#   Escape Characters     ------
# print("Name: xyz\nAge: 25\nCity: Delhi")   # \n = New line
# print("Name:\txyz\tAge:\t25")               # \t = Tab
# print("Path: C:\\Users\\xyz")               # \\ = Backslash
# print('It\'s a good day')                   # \' = Single quote
# print("He said \"Hello\"")                  # \" = Double quote
# print("Hello\rWorld")                       # \r = Carriage return
# print("Helloo\b")                           # \b = Backspace
# print("Hello\fWorld")                       # \f = Form feed
# print("Hello\vWorld")                       # \v = Vertical tab
# print("Hello\a")                            # \a = Alert/Bell
# print("Hello\0World")                       # \0 = Null character



#-----------------------------------------------------------------------------------------------------------------


#List - Anything can be store - mutable -   duplicate   -   ordered.

#list_name = ["A", "B", "C", 21, 15, 11, 15, False]

# print(list_name)


# #--Update
# list_name[2] = "G"
# print(list_name)

# list_name.append("P")             - insert element at end
# print(list_name)

# # insert - list_name(index, value)            - insert by index at any postion
# list_name.insert("1", 15)

# # Extend                             - insert as many at end
# list_name.extend([60, 70])
# print(list_name)

# #--Acess index
# print(list_name[2:5])

# list_name.sort()
# print(list_name)               
# print(list_name.sort())         # ----- here we recive error because our list contain both str & int

# list_name.reverse()
# print(list_name)

# # count
# print(list_name.count(15))         # --- count no.of time occurs

# # copy
# new_list = list_name.copy()         # create a copy of list
# print(new_list)

# # to remove - pop    list_name.pop(index) - it also print pop value / element
# list_name.pop(1)
# print(list_name)


# # remove
# list_name.remove(15)
# print(list_name)

# # clear - remove all data
# list_name.clear()
# print(list_name)


#--------------------------------------------------------------------------------------------------------

# Tuple - Anything can be stored - immutable.
# Tuple is ordered and allows duplicate values.

# tuple_name = ("A", "B", "C", 21, 15, 11, 15, False)

# print(tuple_name)

# print(len(tuple_name))


#-- Access index
# print(tuple_name[2])


#-- Slicing
# print(tuple_name[2:5])
# print(tuple_name[::-1])                  # reverse


    #-- Update
    # tuple_name[2] = "G"
    # print(tuple_name)
    # ----- ERROR because tuple is immutable


    #-- append
    # tuple_name.append("P")
    # print(tuple_name)
    # ----- ERROR because tuple is immutable

# tuple_name = tuple_name + ("P",)         # alternative using +
# print(tuple_name)


    #-- insert
    # tuple_name.insert(2, "P")
    # print(tuple_name)
    # ----- ERROR because tuple is immutable

# tuple_name = tuple_name[:2] + ("X",) + tuple_name[2:]
# print(tuple_name)


    #-- extend
    # tuple_name.extend([60, 70])
    # print(tuple_name)
    # ----- ERROR because tuple is immutable

# tuple_name = tuple_name + (60, 70)       # alternative using +
# print(tuple_name)


#-- Concatenation
# tuple2 = (10, 20, 30)
# tuple3 = tuple_name + tuple2
# print(tuple3)


    #-- sort
    # tuple_name.sort()
    # print(tuple_name)
    # ----- ERROR because tuple has no sort() method

# numbers = (21, 15, 11, 15)
# new_tuple = tuple(sorted(numbers))
# print(new_tuple)


    #-- copy
    # new_tuple = tuple_name.copy()
    # print(new_tuple)
    # ----- ERROR because tuple has no copy() method


    #-- pop
    # tuple_name.pop(1)
    # print(tuple_name)
    # ----- ERROR because tuple is immutable

# removed = tuple_name[2]
# tuple_name = tuple_name[:2] + tuple_name[3:]
# print("Removed:", removed)
# print(tuple_name)



    #-- remove
    # tuple_name.remove(15)
    # print(tuple_name)
    # ----- ERROR because tuple is immutable

# tuple_name = tuple_name[:4] + tuple_name[5:]   # remove index 4
# print(tuple_name)


    #-- reverse
    # tuple_name.reverse()
    # print(tuple_name)
    # ----- ERROR because tuple has no reverse() method

# print(tuple(reversed(tuple_name)))


#-- count
# print(tuple_name.count(15))               # count no. of times value occurs


#-- Repeat
# print(tuple_name * 3)


#-- MAX / MIN / SUM
# max() and min() need comparable elements.
# sum() is used for numeric values.

# numbers = (21, 15, 11, 15)
# print(max(numbers))                       # largest value
# print(min(numbers))                       # smallest value
# print(sum(numbers))                       # total


#-- index
# print(tuple_name.index(21))               # gives index/position of value



    #-- clear
    # tuple_name.clear()
    # print(tuple_name)
    # ----- ERROR because tuple is immutable

# tuple_name = ()
# print(tuple_name)


#-- in
# print(15 in tuple_name)                    # True - value is present
# print("X" in tuple_name)                   # False - value is not present


#-- not in
# print(20 not in tuple_name)                # True - value is not present
# print(15 not in tuple_name)                # False - value is present


#-- LOOPS
# for x in tuple_name:
#     print(x)


#-- List to Tuple
# list_name = ["A", "B", "C", 21]
# tuple_name = tuple(list_name)
# print(tuple_name)


#-- Tuple to List
# list_name = list(tuple_name)
# print(list_name)


#-- Nested Tuple
# student = ("Bharat", (21, "BCA"))
# print(student[1])
# print(student[1][0])


#-- Single Element Tuple
# a = (10)                                  # int
# b = (10,)                                 # tuple
# print(type(a))
# print(type(b))

#--------------------------------------------------------------------------------------------------------

# Dictionary
# key-value pair.
# mutable
# ordered (preserves insertion order)
# accessed using keys not using index
# duplicate keys are not allowed

# dict_name = {"B": 21, "P": 15, "G": 11, 0: "God"} -------

# print(dict_name)


#-- Access value using key
# print(dict_name["B"])
# print(dict_name[0])


#-- get()
# print(dict_name.get("B"))
# print(dict_name.get("X"))              # None if key does not exist

# print(dict_name.get("X", "Not Found"))        # custom value if key does not exist


#-- items()
# print(dict_name.items())               # returns key-value pairs

#-- keys()
# print(dict_name.keys())                # returns all keys

#-- values()
# print(dict_name.values())              # returns all values


# #-- update()
# dict_name.update({"B": 25})            # update existing key
# dict_name.update({"D": 50})            # add new key
# print(dict_name)


# #-- Add new key-value pair
# dict_name["D"] = 50
# print(dict_name)


#-- Change value
# dict_name["B"] = 100
# print(dict_name)


#-- pop()                                   # remove & print last inserted value
# removed = dict_name.pop("P")
# print(removed)
# print(dict_name)


# #-- popitem()
# removed = dict_name.popitem()
# print(removed)
# print(dict_name)                                # removes the last inserted key-value pair


#-- del                     - remove a pair by key
# del dict_name["G"]                
# print(dict_name)


#-- clear()                                 - remove all pair
# dict_name.clear()
# print(dict_name)
# removes all key-value pairs


#-- copy()
# new_dict = dict_name.copy()
# print(new_dict)


#-- setdefault()
# dict_name.setdefault("D", 50)
# print(dict_name)

# If key exists, value is not changed
# If key does not exist, new key-value pair is added


#-- in
# print("B" in dict_name)                 # checks key
# print("X" in dict_name)                 # False


#-- not in
# print("X" not in dict_name)              # True
# print("B" not in dict_name)              # False


#-- Length
# print(len(dict_name))


#-- Loop through keys
# for x in dict_name:
#     print(x)


#-- Loop through values
# for x in dict_name.values():
#     print(x)


#-- Loop through key-value pairs
# for key, value in dict_name.items():
#     print(key, value)


#-- Check key exists and get value
# if "B" in dict_name:
#     print(dict_name["B"])


# # -- Nested Dictionary
# student = {
#     "name": "Bharat",
#     "marks": {
#         "Python": 90,
#         "Java": 85
#     }
# }
# print(student)

# print(student["marks"])
# print(student["marks"]["Python"])


#-- Dictionary from keys
# keys = ("A", "B", "C")
# new_dict = dict.fromkeys(keys, 0)
# print(new_dict)


#-- Dictionary conversion
# list_name = [("A", 10), ("B", 20), ("C", 30)]
# new_dict = dict(list_name)
# print(new_dict)


# #-- Duplicate keys
# test = {"A": 10, "B": 20, "A": 50}
# print(test)                                       # Last value replaces the previous value



#--------------------------------------------------------------------------------------------------------


# Sets
# unordered -- mutable   -- elements are unique   -- No indexing -- No slicing   #-- No duplicate elements

# e = set()                         # empty set not this, e = {} it give dict

# set_name = {11, 15, 15, "B", "G", "P"}

# print(set_name)
# print(set_name, type(set_name))


#-- Add
# set_name.add(21)
# print(set_name)
# adds one element


#-- Update
# set_name.update([21, 25, 30])
# print(set_name)
# adds multiple elements


#-- Remove
# set_name.remove(15)
# print(set_name)
# removes element
# ERROR if element does not exist


#-- Discard
# set_name.discard(15)
# print(set_name)                       # removes element & NO ERROR if element does not exist


#-- Pop
# removed = set_name.pop()
# print(removed)
# print(set_name)
# removes a random/arbitrary element
# because set is unordered


#-- Clear
# set_name.clear()
# print(set_name)
# removes all elements


#-- Copy
# new_set = set_name.copy()
# print(new_set)


#-- in
# print(15 in set_name)            # True
# print(50 in set_name)            # False


#-- not in
# print(50 not in set_name)        # True
# print(15 not in set_name)        # False


#-- Length
# print(len(set_name))


#==================================================
# SET OPERATIONS

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}


# #-- Union   - Combines elements from both sets
# print(set1.union(set2))
# print(set1 | set2)


# #-- Intersection    - Gives common elements
# print(set1.intersection(set2))
# print(set1 & set2)


# #-- Difference  - Elements present in set1 but not in set2
# print(set1.difference(set2))
# print(set1 - set2)


# #-- Symmetric Difference    - Elements that are NOT common on both
# print(set1.symmetric_difference(set2))
# print(set1 ^ set2)


# #-- Subset  - Checks whether one set is completely inside another
# # -- is set1 is present in set2
# print(set1.issubset(set2))                  #- give true / false


# #-- Superset    - Checks whether one set contains another set
# #-- in set2 set1 is present
# print(set2.issuperset(set1))              #- give true / false


# #-- Disjoint    - Checks whether two sets have NO common elements then TRUE
# print(set1.isdisjoint(set2))


#==================================================
# MODIFYING SETS



# #-- intersection_update()
# # Keeps only common elements but changes orignal set
# set1.intersection_update(set2)
# print(set1)



# #-- difference_update() - Removes common elements from set1 & changes the original set1
# set1.difference_update(set2)
# print(set1)


# #-- symmetric_difference_update()       -  Keeps elements that are not common
# set1.symmetric_difference_update(set2)
# print(set1)



#==================================================
# SET CONVERSION


# #-- List to Set
# list_name = [10, 20, 20, 30, 30]
# set_name = set(list_name)
# print(set_name, type(set_name))



# #-- Tuple to Set
# tuple_name = (10, 20, 20, 30)
# set_name = set(tuple_name)
# print(set_name, type(set_name))


# #-- Set to List
# list_name = list(set_name)
# print(list_name, type(list_name))




#------------------------------------------------------------------------------------------------------------

# Conditional Expressions       - code that lets a program take a decision. It runs a block only when a condition is True.

# 1. IF ELSE & ELIF
                        # - here we can use   'and'     'or'    'not'

# if(cond...):
#     print("xyz")
# elif(cond...):
#     print("xxx")
# elif(cond...):
#     print("zzz")
# else:
#     print("zyx")

# *** always remeber if a condn stisfy at if and elif both places, we only consider if then code terminate.

# var_name = "xyz"
# if var_name == "xyz" or var_name == "zyx":
#     print("asdfghj")


# var_name = 00
# if var_name >= 00 and var_name <= 11:
#     print("asdfghj")



# 2. CASE - SWITCH CASE

# vari_name = 2  (case no.)     or can use as user input for case

# match vari_name:
#     case 1:
#         print("x")
#     case 2:
#         print("y")
#     case 3:
#         print("z")
#     case _:
#         print("...")



#------------------------------------------------------------------------------------------------------------

# Loops     - a structure that repeats a block of code. One repetition is called an iteration. 
# For & while 

#   --  While loops --- repeats as long as its condition is True. It is used when you do not know in advance how many times to repeat.

# i = x             intialize
# while(cond...):
#     print("xyz")
#     i += x            update / increment in i then check cond, if satisfy then terminate.

# #ex

# i = 1                  # initialise
# while i < 6:           # condition
#     print(i)
#     i += 1             # update



# # --  print list using while Look --  
# ls = [11,15,15,"g","B","p", False]
# i = 0
# while(i<len(ls)):                 # len(ls) - len of list
#     print(ls[i])                # ls[i] - i index - index printing
#     i+=1




#   --  For loop    ---- it itrate till cond is stisfiyed.

# for i in range(int, end, inc):
#     print(i)


# #ex. 4 table
# for i in range(0, 40, 4):
#     print(i)


# #   --  print list using for loop   --
# ls = [11,15,15,"g","B","p", False]
# for i in ls:
#     print(i, type(ls))


# #   --  print tuple using for loop   --
# tp = (11,15,15,"g","B","p", False)
# for i in tp:
#     print(i, type(tp))


# #   --  print string using for loop   --
# g = "tiwar ji"
# for i in g:
#     print(i)
# else:
#     print("might be")



#==========================================================

#   --  Break   --
#     - instant exist the loop. it kill the loop.
# for i in range(11,21):
#     if(i==15):
#         break
#     print(i)


#   --  continue    --
#     - if condn. meet, skip the curreent iteration and continue iteration.
# for i in range(11,21):
#     if(i == 15):
#         continue
#     print(i)


#   --  pass    --
#     - it a null statement means it excute to do nothing.

# for i in range(11,21):
#     pass

# i =11
# while(i<21):
#     print(i)
#     i+=1


#------------------------------------------------------------------------------------------------------------

# Recursion and function

# Function
    # - group of statement perform specific task. reuseable, no repeated code.
    # - # 1. Built in fxn - already provided functions like print(), len(), range() etc.
        # 2. User defined fxn - user made like greet() below.


# def fxn_name( parameters ):
#     {
#         logic...
#         print("xyz")
#     }

#     fxn_name( arguments )      - to call fxn


# Parameter - the placeholder variable written in the function definition. like n, endingg.
# Argument - the actual value you pass / give when calling the function. like n = name & endingg = thank you.
# below example


# def add(a, b):
#     return a + b

# result = add(3, 4)    # result stores 7


# # ex -----

# def greet():                         
#         print(n + " " + "have a good day !")

# n = str(input("enter you name : "))     
# greet()            

#==================================

# # ex ----- here we give parameter and arguments  //    1 parameter with many arugments

# def greet(n, endingg):                            # - n & endingg are parameters
#         print(n + " " + "have a good day !")
#         print(endingg)

# #n = str(input("enter you name : "))      # # to use n, remove n from fxn parameter and arguments
# greet("god", "thanks!!")                          # - here n = god & endingg = thank are arguments value given to parameters.
# greet("Shyam", "Goodbye!")


#==================================

# # here when we print a we need return value that a printed

# def greet(n, endingg): 
#         print(n + " " + "have a good day !")
#         print(endingg)

#         # return"done"
#         return 7

# a= greet("god", "thanks!!")
# print(a)


#==================================

# # Here the ending is by default print parameter value

# def greet(n, endingg = "jai ho !!"): 
#         print(n)
#         print(endingg)

# greet("god")            # - here we didn't give ending what to print but by default value it print.




#==================================


# --    Recursion ---   when a function calls itself to solve a smaller version of the same problem.
#     - Base case: the condition that stops the recursion. Without it the function calls itself endlessly and Python raises a RecursionError.
#     - Recursive case: the step where the function calls itself with a smaller input.


# Ex - factorial

# factorial(5) = 5 × 4 X 3 X 2 X 1   -      5 * fact(4)
# factorial(4) = 4 × 3 X 2 X 1       -      5 * 4 * fact(3)
# factorial(3) = 3 X 2 X 1           -      5 * 4 * 3 * fact(2)
# factorial(2) = 2 X 1               -      5 * 4 * 3 * 2 * fact(1)
# factorial(1) = 1                   -      5 * 4 * 3 * 2 * 1 * fact(0)


# factorial(n) = n   *   n-1    *   n-2    *       n-3 .....

# factorial(n) = n * factorial(n-1)

# def fact(n):
#     if(n==1 or n==0):               # - must Base condn.
#         return 1
#     return n * fact(n-1)
    

# n = int(input("give n : "))
# print(fact(n))





#------------------------------------------------------------------------------------------------------------

# File I/O - It means using Python to store data in files and retrieve that data later.


# operations :    r - read    w = write   r+ - read & Write   a - append    x - create a new file.

# open() - open a file.

# f = open("file_address","opration")
# content = f.read()

# f.write("xyz")
#       #or
# xx = "Welcome to Python."
# f.write(xx)

# print(content)
# f.close()                      # - close file manually



# # 'with open()' automatically closes files

# with open("file.txt", "r") as f:              # as f - means store file contnet in f variable.
#     print(f.read())
#       #or
#     print(f.readline())                      # read a single line.



# with open("file.txt", "r") as f:
#     print("Stored name:", f.read())


# with open("file.txt", "r") as f:
#     lines = f.readlines()                                     # give list as result.
# print(lines)


# using while loop to read files line
# line = f.readline()
# while(line != ""):
# print(line)
# line = f.readline()

# f.close()


# with open("file.txt", "w") as f:
#     f.write("Learning File I/O")


# # using append
# with open("file.txt", "a") as f:
#     f.write("\nLearning File I/O.")


# name = input("Enter your name: ")
# with open("file.txt", "w") as f:
#     f.write(name)



# # write multiple line as list
# lines = ["Bharat\n", "Gauri\n", "Soni\n"]
# with open("file.txt", "w") as f:
#     f.writelines(lines)



# # creating a new File
# with open("newfile.txt", "x") as f:
#     f.write("My first file!")



# # handle error while opening file                  - Opening a missing file raises FileNotFoundError.
# try:
#     with open("missing.txt", "r") as f:
#         print(f.read())

# except FileNotFoundError:
#     print("The file does not exist!")



# # Rename a file
# from pathlib import Path

# old_file = Path("file.txt")
# old_file.rename("new.txt")


# # Delete a file
# from pathlib import Path                          # pathlib - library work with paths
# file = Path("new.txt")

# if file.exists() and file.is_file():
#     file.unlink()
#     print("File deleted!")


#==================================

# # Work with CSV file 

# # Read ---

# import csv

# with open("file.csv", "r", newline="", encoding="utf-8") as f:
#     reader = csv.reader(f)

#     for row in reader:
#         print(row)


# # Write ---

# import csv

# with open("file.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.writer(f)

#     writer.writerow(["Name", "Marks"])
#     writer.writerow(["Bharat", 90])
#     writer.writerow(["tiwari ji", 90])

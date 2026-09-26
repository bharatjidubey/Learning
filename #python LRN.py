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

# print()
# to print simple string - print(" xyz ")
# print(x, y, z)
# print(x + y + z)
# to print mutilines use triple single / double qoute - print(''' xyz ''')

# print(" xyz ")
# print(''' x
#     y
#         z ''')


#--------------------------------------------------------------------------------------------------------

# vsriable - A container - it stores values like intereger string etc.
# variable name should be not any keyword, _aa , aa_aa , valids incliding numeric.
# variable name start with slphabate underscore but not numeric in mid underscore valid, and numic also valid in mid.

#x = y = z = "Orange"  //  x, y, z = "Orange", "Banana", "Cherry"

# CAsting - changing data tyoe. 
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

# Example                         Data Type

# x = "Hello World"               str
# x = 20                          int
# x = 20.5                        float
# x = 1j                          complex
# x = ["apple", "banana", "cherry"] list
# x = ("apple", "banana", "cherry") tuple
# x = range(6)                    range
# x = {"name": "John", "age": 36} dict
# x = {"apple", "banana", "cherry"} set
# x = frozenset({"apple", "banana", "cherry"}) frozenset
# x = True                        bool
# x = b"Hello"                    bytes
# x = bytearray(5)                bytearray
# x = memoryview(bytes(5))        memoryview
# x = None                        NoneType

#--------------------------------------------------------------------------------------------------------

# operators & operands

# operands are variable and operators are = + - * etc

# 1. Assignment operator
# 2. comperision operator
# 3. arithmatic operator
# 4. logical operators




# a =+ 2    means a =  a + 3 = ...

#--------------------------------------------------------------------------------------------------------

#Strings - these are immutable orignal string not change, a new changed string should print.

# print(" xyz ")
# print(''' x
#     y
#         z ''')


# looping
# for x in "banana":
#   print(x)


# Check fxn - To check if a certain phrase or character is present in a string, we can use the keyword in.
# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# print("expensive" not in txt)


# if function - 
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

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


#print(len("hello"))       or    print(len(b))      - count space

#print(b.lower())       or    print("xyz".upper()) 
#print(b.upper())       or    print("xyz".upper()) 

#print(b.replace())
#print(b.find("xyz"))
#print(b.replace("old", "new", 1))    or        #print(b.replace("old", "new", 1).replace("xx", "yy")) -  1 means only 1 time replace.

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

# Escape Characters
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
# print("Hello\0World")                        # \0 = Null character


#   Taking Inputs
#vari_name = input("enter xyx : ")
#print(f"xyz,{vari_name}") - via f we can use variable at mid of string  or      print("xyz", vari_name)  



#-----------------------------------------------------------------------------------------------------------------


#List - Anything can be store - mutable.
list_name = ["A", "B", "C", 21, 15, 11, 15, False]

# print(list_name)


# #--Update
# # list_name[2] = "G"
# # print(list_name)

# # list_name.append("P")
# # print(list_name)

# # insert - list_name(index, value)
# list_name.insert(0, 15)

# # #--Acess index
# # print(list_name[2:5])

# # list_name.sort()
# # print(list_name)               
# # print(list_name.sort()) ----- wrong

# list_name.reverse()
# print(list_name)


# # to remove - pop    list_name.pop(index)
# list_name.pop(1)
# print(list_name)






          
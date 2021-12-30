"""
print, input

4 data types
    integers-whole numbers which include negatives and zero( numbers without decimals)
    floats- numbers with decimals
    strings- text, a sequence of charecters
    letters(capital and lowercase), numbers, symbols, @#$%^&
    bools- True, False

    None - IT EXISTS

is zero even - yes
definition of 0 --2k=0 to test if it is even, 2k+1 =0 to test if odd
"""
my_variable = 17
# an assignment is when a value is placed inside a variable
# a declaration is when we tell python (interpreter/compiler/machine) that a specific variable exist

"""
    In python the first assignment of a variable is its declaration.
"""
My_int = 5

# some code here

print(My_int)
My_int = 13
print(My_int)

My_int= 2*My_int+5
print(My_int)

# you can always reassign variables
other_int = 3 # always assign variables before putting them together
My_int = other_int + 8
print(My_int)

# x + 5 = 12, python does not do math functions to solve for x
V=12
t= 5
#LHS must be a single variable
#RHS can be anything python can evaluate
x= V-t

#python is not a typed language
x= "now i am a string"
print(x)
print(type(x))

"""
    casting
"""
#my_fav_integers= int(input("tell me your favorite integer"))
#print(my_fav_integers, my_fav_integers + 17)

# int("hello")
# for most of this class you can assume the end user will enter the correct data type

"""
    PEP8 - coding style
    variable names should be lowercase seperated by underscores
    
    python - variable must start with a letter or underscore, and be composed of
    letters, numbers, and underscores
"""
something = False
# if statements
if something:
    print("something was true")
    # tab in one level to be inside of statment

# anything not tabbed will just run, not be inside the if

test_var = 17
my_car = 'camry'

if my_car == "accord":
    print('feels bad...')
if my_car == "camry":
    print("hello professor, i am your car")

    # most languages use this convention where == is the comparison

if test_var < 213:
    print('test var was smaller than a random number')

"""
comparisons:
    ==, <,>,<=,>=,!=
    NEVER: is
"""
if 3<=5:
    print("congrats")

""""
     3 types of operators:
     Arithmetic(goes first, highest precedence):
     +,-,*,/,//,**(not obvious, not ^)
     
     comparisons( goes second, middle precedence):
    ==, <,>,<=,>=,!=
    
    logical(goes last, last precedence):
    and, or
    not    
"""
x=3
if 3+x == 8:
    print("yep that's right")

if x ==3 or x == 4:
    print(' x is either 3 or 4')
elif x==10:
    print(" this is correct use of elif statement")

"""
Or  T   F
 T    T   T
 F    T    T
"""
if x== 3 or x ==4:
    print('x is either 3 or 4')
if x==3 or 4:
    print("what is wrong with me")
if -31:
    print("not zero? what is this?")
if 0:
    print("never sad...")

if "hello":
    Print("hello is true, i dont understand this")
if "False":
    print("false is true")
if "":
    print("empty string hapens to be false")

# in int 0 is false anything else is true, in string emotty string is false anything else is true.


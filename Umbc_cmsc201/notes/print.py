print('stuff')
print("stuff")

print(17)
print(42)
print(3.14159265358979)
print(1.618)
print(6.9)
print(-8.75)
print(18.0)
# float = double high precision

print(True, False)
print(True *False)
"""
multi-line comment
  Python compiler/interpreter doesn't read this
  data types:
  string - a "list" of chractrers / text / raw input
  integers - whole numbers, negative whole numbers,
  float - whole numbers, negative whole numbers, zero
  Boolean - true or false

  none

"""
print(None)
#single line comment
print("python", "is", "a", "fun", "language")
print("python", "is", "a", "fun", "language", sep='a')
#you can print multiple types in the same print statement
print("hello there", 56, 1.618, True)
#you can concatenate
print("this is" + " "+ "concatenation")
print("hello my favorite number is: ", + 17)

# casting allows us to convert between data types
print("hello my favorite number is: " + str(17))

"""
what other kind of casting can we do?
str -> int
string -> float

float->str
int->str

float->int

"""
print(int(3.14), int(3.99))
#value error, do not uncomment
#float("hello there")

print(float(57))

s = input()
# if you need to print it out
#print(s)
#print(input())
#other_string = input('Tell me an adjective: ')

an_integer = int(input('Tell me an integer: '))
print(type(an_integer))
a_floaty = float(input('Tell me as many digits of e as you know: '))
# non-typed language python is a lnaguage without type specifiers required for each
# a language where you can assign new types to old variables
an_integer = "this is now a string"
print(an_integer)
print(5 * an_integer)

"""
Variable Declarations
something we stick into ram
Ram = Random Access Memory
Every place in ram has a numerical address
Programming languages hide the addresses from us and use names instead

Rules for python variable name:
1)Start with an underscore or letter (not number)
2)Only composed of uppercase, lowercase letters numbers and underscore

Lowercase letters separated by underscore (PEPS style)


"""
A_sTrInG = 'this is a pretty cursed variable name'

__my_integer = 3

my_variable = 6

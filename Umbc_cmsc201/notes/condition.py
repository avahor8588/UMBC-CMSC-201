"""
    if statments

    you can have as many elifs as you want to

"""
"""
condition = True
other_condition = False
if condition and \
        other_condition:
    print('the condition is true')
else:
    print("the condition was false")

x = int(input("tell me a number "))
if x ==1:
    print("x was 1")
elif x ==2:
    print("x was 2")
elif x ==3:
    print("x was 3")
elif x ==4:
    print("x was 4")
elif x ==5:
    print("x was 5")
elif x==2:
    print("robot evolution")
else:
    print("x was not between 1 and 5 inclusivley")
"""
a = True
b = False
c = False
d = True
e = False
if (a and b) or c:
    print("it is on")
else:
    print("it is off")
if a and b or c:
    print("yes")
else:
    print('no')

if not ((a and b) or (not d or e) or c):
    print("something happened")
else:
    print("nothing happenend")
# not (a or b) = not a and not b
# not (a and b) = not a or not b
if not (a or b):
    print("demorgans")
if not a and not b:
    print("also demorgans")

a = False
b = False
c = True
d = True
e = True

if (a and not b) or not (c and d and e):
    print("what the heck is this?")
# a = true as long as b = true
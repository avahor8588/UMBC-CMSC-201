print(5/3)
#integer division
print(5//3)
print(24//5)
print(17//6)
print(-5//7)
"""
n= d*q +r
rule r>=o
remainder has to stay positive
"""
print(-12//7)

"""
    let's talk about mod
    
    short for modulus
    
    demonstrated by %
"""


"""    
print(5 % 3)
# shows remainder
print(271 % 5)
print(-17 % 5)
print(63 % 9)
print(4%2) # 2 goes into 4 twice so remainder is zero
print(2%4) # 4 goes into 2 0 times so remiander is 2
"""

an_integer = int(input("tell me an integer: "))
if an_integer != 0:
    print(1729 // an_integer)
    print('hello there')
    print('something else')
    print('more stuff')
print("not in the if statement")
# sequential control flow

if an_integer % 2:
    print(' our integer is....odddd')

# if the first statement is TRUE it Wont execute
# guarentees that if the first statement are false, it wont execute
if an_integer % 2 ==0:
    print(' our integer is even?????')
else:
    print('our integer is even!, (not odd)')

day_of_month = int(input(' what day of the month is it?'))
"""
    calculate the day of the week
    a) we know that wed = 1
    b) day +/- 7 = same day
        b.1) day % mod 7 is that always the same?
        
    else if = english version
    elif = python version
"""
if day_of_month % 7 ==1:
    print("this is wednesday")
elif day_of_month % 7 == 2:
    print("this is thursday")
elif day_of_month % 7 ==3:
    print("this is friday")
elif day_of_month % 7 ==4:
    print("this is saturday")
elif day_of_month % 7 ==5:
    print("this is sunday")
elif day_of_month % 7 ==6:
    print("this is monday")
elif day_of_month % 7 ==0:
    print("this is tuesday")
else:
    print('huh?')

your_name = input('tell me your name: ')
if "$" in your_name:
    print("we don't allow that")
elif "@" in your_name:
    print("not that one")
elif "^" in your_name:
    print("we don't allow charecters.")
else:
    print('all good')
"""
     nest if statements
        if you stick an if statement into an if statement
"""

#original series

human = input('are youa human')
if human =="yes":
    are_you_giving_it_all_shes_got_captain = input(' are you giving it alss she\'s got captain')
    if are_you_giving_it_all_shes_got_captain == 'yes':
        print(' you are scott')
    else:
        drinking_how_is_that = input('do you like to dirnk a lot')
        if drinking_how_is_that =="yes":
            print('you are doctor')
        else:
            sword_fighting = input('do you like swords')
            if sword_fighting == "yes":
                print('you are sulu')
            else:
                print('kirk out')

else:
    vulcan = input(' are you vulcan')
    if vulcan == "yes":
        print('your are spock. ')
    else:
        print(' are you are uhuaru')

"""
    leap years
    
        if years div by 4, leap year...
            except if it's divisible by 100... not
                except if its divisble by 400...is again...

"""

year =int(input("tell me the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
        print(" this is a big leap year")
    else:
        print("this is not a leap year")
 else:
     print('this is a leap year')




else:
    print("this is a leap year")


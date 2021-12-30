"""
Recursion:
    tutrtles all the way back

    functions that call themselves

    we need a base case thhat tell us where to stop

"""

def countdown(x):
    if x<0:
        print("blast off")
        return
    else:
        print(f"t = {x}")
        countdown(x-1)

#countdown(17)

"""
    factorials
    0!=1
    abc, acb,bac, cba 

"""

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))

def search(the_grid, current_pos):
    y, x = current_pos
    search(the_grid, (y-1,x))
    search(the_grid, (y-1,x))
    

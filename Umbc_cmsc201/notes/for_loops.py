"""
    print/ input
    variables
    arithmatic/ algebra
    if statements
    for loops <-- code that repeats

"""
# i is the index of the loop, dummy variable
"""
for i in range(10):
    print(i)

endpoint = int(input(" how many times do you want to loop?"))
the_sum =0
for j in range (endpoint):
    the_sum += j

the_sum = endpoint
for j in range(endpoint):
    the_sum +=j
"""
endpoint = int(input(" how many times do you want to loop?"))
the_sum = 0
for j in range(endpoint):
    the_sum += j +1

print(the_sum)

endpoint = int(input(" how many times do you want to loop?"))
factorial = 1
for k in range(1, endpoint + 1):
    factorial *= k

print(factorial)

# fibonnaci numbers
which_fib = int(input("which fibonnoci number do you want to calculate? "))
previous_fib = 1
previous_previous_fib = 1
current_fib = 1
for i in range(2, which_fib):
    print(current_fib, previous_fib, previous_previous_fib)
    current_fib = previous_fib + previous_previous_fib
    previous_previous_fib = previous_fib
    previous_fib = current_fib
print(current_fib)

# prime  number is a number divisble by itself and one.
# skip 0 because of divison by zero and skip 1 bc everything divides by 1
is_prime = True
test_int = int(input("what number do you think is prime? "))
for i in range(2, test_int):
    if test_int % i == 0:
        print(1, "not prime")
        is_prime = False

if is_prime:
    print(" it is prime")




"""
File:         robot_test.py
Author:       Aamil vahora
Date:         9/20/2021
Section:      42
E-mail:       amilv1@umbc.edu
Description:  YOUR DESCRIPTION GOES HERE AND HERE
              YOUR DESCRIPTION CONTINUED SOME MORE
"""

robot = input("Be you robot, or human? ")
if robot == "human":
    print("Humans must be destroyed! ")
elif robot == "robot":
    print("Administer the test!")
    print("Which of the following would you prefer? ")
    print("A cute (puppy)")
    print("A (flower) from your sweetie")
    print("A large properly formatted (data file).")
    choose = input("choose: ")
    if choose == "puppy":
        print("Get the intruder! Get the humanoid!")
    if choose == "flower":
        print("That is acceptable, pass on mechanical friend.")
    elif choose == "data file":
        print("Very good, you are a robot of some esteem. ")



Q1 = input("Are you a hero or a villain?")
if Q1 == "villan":
     name = input("what is your name")
     print(f"{name} sounds pretty evil!")
elif Q1 == "hero":
     p = int(input("how many people have you saved"))
# the next if statment is in the  first(which is why it is indented)
     if p <= 10:
          print("Go on more patrols!")
     elif p > 10 and p < 100:
          print("sounds like your making a difference!")
     elif p>=100:
          print("Wow, great job saving the city!")
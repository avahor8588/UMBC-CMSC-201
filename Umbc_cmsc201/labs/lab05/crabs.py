stop = "STOP"
x= 0
list =[]
wieght= float(input("Enter crab weight, (STOP to end)"))

while wieght != stop:
    list.append(float(wieght))
    wieght= (input("Enter crab weight, (STOP to end)"))


light_or_heavy = input("Do you want to keep light or heavy crabs?")
while light_or_heavy != "light" and light_or_heavy != "heavy":
    print(" Please try again")
    light_or_heavy = (input("Do you want to keep light or heavy crabs?"))

list_heavy = []
list_light =[]
if light_or_heavy == "light":
    determines = float(input("What weight determines whether a crab is light or heavy?"))
    for value in list:
        if value < determines:
            list_light.append(value)
        else:
            list_heavy.append(value)
    print("You are keeping the crabs with weights", list_light)
    print("You are not keeping the crabs with weights", list_heavy)



if light_or_heavy == "heavy":
    determines = float(input("What weight determines whether a crab is light or heavy?"))
    for value in list:
        if value > determines:
            list_heavy.append(value)
        else:
            list_light.append(value)
    print("You are keeping the crabs with weights", list_heavy)
    print("You are not keeping the crabs with weights", list_light)














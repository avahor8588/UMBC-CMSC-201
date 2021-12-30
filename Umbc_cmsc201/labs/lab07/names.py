

def sum_list(numbers):
    suum = 0
    for i in numbers:
        suum += i

    return suum
        

def get_string_lengths(strings):
    list_two = []
    for value in range(len(strings)):
        list_two.append(len(strings[value]))
    return list_two

def get_names():
    names_list = []
    names = input("Enter a name, STOP to stop: ")
    while names != "stop" and names != "STOP":
        names_list.append(names)
        names = input("Enter a name, STOP to stop: ")

    return(names_list)

if __name__ == '__main__':
    kitties = [
        "Jules",
        "Stubby",
        "Tybalt",
        "Scooter",
        "KC",
        "Garfield",
        "Bucky"
    ]
    output = (sum_list(get_string_lengths(kitties)))
    print(f"There are {output} letters in kitties.")

      

    puppers = [
        "Charlie",
        "Chuck",
        "Chuckadero",
        "Char",
        "Charmander",
        "Charles, Lord of Hearts, King of Snuggles"
    ]

    output = (sum_list(get_string_lengths(puppers)))
    print(f"There are {output} letters in kitties.")



    name = get_names()

    output = (sum_list(get_string_lengths(name)))
    print(f"there are {output} letter in the names you eneterd")

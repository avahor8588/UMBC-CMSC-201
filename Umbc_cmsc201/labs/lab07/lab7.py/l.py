def sum_list(numbers):
    list = []
    for i in numbers:
        list.append(i)
    out = "".join(list)
    print(len(out))

        

def get_string_lengths(strings):
    list = []
    for i in strings:
        list.append(i)
    out = "".join(list)
    print(len(out))

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
    sum_list(kitties)
    
      

    puppers = [
        "Charlie",
        "Chuck",
        "Chuckadero",
        "Char",
        "Charmander",
        "Charles, Lord of Hearts, King of Snuggles"
    ]

    sum_list(puppers)
    
    name = get_names()

    sum_list(name)
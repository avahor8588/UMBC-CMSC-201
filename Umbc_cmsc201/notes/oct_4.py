
"""
    strips
         removes witesapces from the end and begining of a string
    split
    join
"""
if False:
    # strip command gets rid of the spaces in begining and end of string
    story = input("tell me a story: ")
    print(story.strip())

    # ints and floats are pre stripped
    five = ("   5   ".strip())
    print(five)

string = input("tell me something: ")
print(string.split(","))

"""
    split takes a string and makes it a list
    join takes a list(of strings) and makes one big string
"""
fav = ['banana', 'watermelon', 'apple', 'nsb']
sperator = input("tell me a seperator: ")
print(sperator.join(fav))

"""
    python -strings are immutable(cannot be chnaged)
"""
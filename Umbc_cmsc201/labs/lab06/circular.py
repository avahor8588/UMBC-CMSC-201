"""
File:         circular.py
Author:       Aamil vahora
Date:         3/18/2020
Section:      42
E-mail:       aamilv1@umbc.edu
Description:  finding offset of a string
"""

if __name__ == '__main__':
    question = input('Enter a string: ')
    question_split = question.split()
    string = ''.join(question_split)
    the_String = string.lower()
    final_string = ''

    my_list = []
    for i in range(len(the_String)):
        if the_String[i] != '':
            final_string += the_String[i]
    for offset in range(len(final_string)):
        rotation = True
        for i in range(len(final_string)):
            if(offset == 0):
                rotation = False
            if final_string[i] != final_string[(i + offset) % (len(final_string))]:
                rotation = False
        if rotation:
            print(question, 'rotation with offset: ', offset) 
            my_list = list(str(offset))

    if (my_list):
        include_num = True
    else:
        print("There are no rotations of the string.")






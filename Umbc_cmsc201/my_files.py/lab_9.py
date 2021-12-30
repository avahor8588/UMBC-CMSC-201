def odd(the_list):
    my_list_list  = []
    for value in the_list:
        count = 0
        for i in value:
            if i% 2== 1:
                count+=1
        my_list_list.append(count)
    return my_list_list









list = [[2,2], [3,4]]

print(odd(list))
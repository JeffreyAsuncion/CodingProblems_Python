"""
Consider a list (list =[])  You can perform the following commands.

1. insert i e : Insert integer e at position i
2. print : Print the list
3. remove e: Delete the first occurence of integer e
4. append e : Insert Integer e at the end of the list
5. sort : Sort the list
6. pop : Pop the last element from the list
7. reverse: Reverse the list

Initialize your list and read in the value of n followed 
by n lines of commands where each command will be
of the 7 types listed above. Iterate though each command in order and 
perform the corresponding operation on your list
"""

def func_insert(lst, i, e):
    #print("\ncalling insert function")
    lst.insert(i, e)
    return lst

def func_print(arg):
    #print("\ncalling print function")
    print(arg)

def func_remove(lst, e):
    lst.remove(e)
    return lst

def func_append(lst, e):
    #print("\ncalling append function")
    lst.append(e)
    return lst

def func_sort(lst):    
    #print("\nCalling Sorting function")
    lst.sort() # note the original array is modified
    return lst

def func_pop(lst):
    #print("\ncalling Pop Function")
    lst.pop()
    return lst

def func_reverse(lst):
    #print("\nCalling Reverse List Function")
    lst = lst.reverse()
    return lst

# http://openbookproject.net/pybiblio/tips/wilson/dictionaryMenus.php
if __name__ == '__main__':
    # read in N num of commands and then commands
    N = int(input())

    raw_command_list = []
    for _ in range(N):
        choice = str(input())
        raw_command_list.append(choice)

    #print(raw_command_list)
    arr = []
    commands = []
    for command in raw_command_list:
        lst = command.split()
        commands.append(lst)
        if lst[0] == "insert":
            i = int(lst[1])
            e = int(lst[2])
            func_insert(arr, i , e)
        elif lst[0] == "print":
            func_print(arr)
        elif lst[0] == "remove":
            #if arr != []:
            e = int(lst[1])
            arr = func_remove(arr, e)   
        elif lst[0] == "append":
            e = int(lst[1])
            func_append(arr, e)
        elif lst[0] == "sort":
            func_sort(arr)
        elif lst[0] == "pop":
            func_pop(arr)
        elif lst[0] == "reverse":
            func_reverse(arr)

    
    """
    arr = [1, 2, 3]
    print(array)


    #1. insert i e : Insert integer e at position i
    i = 2
    e =100

    func_insert(arr, i, e)
    print(arr)

    #2. print : Print the list
    func_print(arr)

    #3. remove e: Delete the first occurence of integer e
    e = 3
    func_remove(arr, e)
    print(arr)

    #4. append e : Insert Integer e at the end of the list
    e = 40
    func_append(arr, e)
    print(arr)

    #5. sort : Sort the list

    sort_arr = func_sort(arr)
    print(sort_arr)

    #6. pop : Pop the last element from the list

    func_pop(arr)
    print(arr)

    #7. reverse: Reverse the list
    print(func_reverse(arr))
    """
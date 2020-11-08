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
    print("\ncalling insert function")
    lst.insert(i, e)
    return lst

def func_print(arg):
    print("\ncalling print function")
    print(arg)

def func_remove(lst, e):
    print("\ncalling remove function")
    lst.remove(e)
    return lst

def func_append(lst, e):
    print("\ncalling append function")
    lst.append(e)
    return lst

def func_sort(lst):    
    print("\nCalling Sorting function")
    lst = sorted(lst) # note the original array is not modified
    return lst

def func_pop(lst):
    print("\ncalling Pop Function")
    lst.pop()
    return lst

def func_reverse(lst):
    print("\nCalling Reverse List Function")
    return lst[::-1]


if __name__ == '__main__':
    N = int(input())

    arr = [1, 2, 3]
    print(arr)


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
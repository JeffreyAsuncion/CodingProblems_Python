# # find out why this is broken
# num_times = 0

# def pac_man(cow, num_times):
#     print("running")
#     if cow == 0:
#         # print(num_times)
#         return num_times

#     else:
#         cow -= 1
#         print(f"Chomp {cow}")
#         num_times += 1
#         pac_man(cow, num_times)
#         # print(num_times)
#     # return num_times

# print(pac_man(20,0))

# count = 0
def pac_man(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        print("Chop!")
        # count += 1
        return (pac_man(x-1))


pac_man(20)
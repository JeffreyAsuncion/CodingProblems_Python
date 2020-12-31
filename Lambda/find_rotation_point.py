"""
I was bored one day and decided to look at last names in the phonebook for my
area.
I flipped open the phonebook to a random page near the middle and started
perusing. I wrote each last name that I was unfamiliar with down on paper in
increasing order. When I got to the end of the phonebook, I was having so much
fun I decided to start from the beginning and keep going until I reached the
page where I had started.
When I was finished, I had a list of interesting last names that were mostly
alphabetical. The problem was that my list starts somehere near the middle of
the alphabet, reaches the end, and then starts from the beginning of the
alphabet. In other words, my list of names is sorted, but it is "rotated."
Example:
surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]
Write a function that finds the index of the "rotation point". The "rotation
point" is where I started working from the beginning of the phone book. The
list I came up was absolutely huge, so make sure your solution is efficient.
*Note: you should be able to come up with a solution that has O(log n) time
complexity.*
"""

"""
Brute Force
"""
def find_rotation_point(surnames):
    # Linear Search (Brute Force)
    # iterate over the surnames list
    for i in range(len(surnames)):
        # check if surnames at index of n1 is 
        # greater than surnames at index n2
        if surnames[i]>surnames[i+1]:
            # return the index   i + 1
            return i + 1 


# def find_rotation_point(surnames):

#     """01:30 """
#     # Your code here
#     # Linear Search (Brute Force)
#     # set 2 indices n1 and n2
#     # iterate over the surnames list using a range based loop
#         # check if surnames at index of n1 is greater than
#         # surnames at index n2
#             # return n2
#         # increment n1
#         # increment n2
#     pass



surnames = [
    'liu',
    'mcdowell',
    'nixon',
    'sparks',
    'zhang',
    'ahmed',  # <-- rotates here!
    'brandt',
    'davenport',
    'farley',
    'glover',
    'kennedy',
]

print(find_rotation_point(surnames))
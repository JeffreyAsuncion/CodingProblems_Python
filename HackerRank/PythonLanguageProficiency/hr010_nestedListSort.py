
# https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/

"""
Given the names and grades for each student in a class of N students, 
store them in a nested list and 
print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
"""


if __name__ == '__main__':
    # inputs list of students in a list
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([str(name), score])
    
    # sort list by score
    sorted_students = (sorted(students, key = lambda x: x[1]))    
    # first index has lowest score
    min_score = students[0][1]
    print(min_score)
    
    

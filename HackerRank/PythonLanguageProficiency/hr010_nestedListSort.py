
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
    """
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([str(name), score])
    """
    students = [["Harry",37.21], ["Berry",37.21], ["Tina",37.2],["Akriti",41],["Harsh",39]]
    # sort list by score
    sorted_students = (sorted(students, key = lambda x: x[1]))   
    # first index has lowest score
    min_score = sorted_students[0][1]
    #print(min_score)
    i = 0
    for i in range(len(sorted_students)):
        if sorted_students[i][1] > min_score:
            secondMinScore = sorted_students[i][1]
            break
    #print(secondMinScore)
    students2ndmin = []
    i=0
    for i in range(len(sorted_students)):
        if sorted_students[i][1] == secondMinScore:
            students2ndmin.append(sorted_students[i][0])
            #print(sorted_students[i])
    students2ndmin = sorted(students2ndmin)
    for name in students2ndmin:
        print(name)
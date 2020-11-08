"""
The provided code stub will read in 
a dictionary containing key/value pairs of 
name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, 

showing 2 places after the decimal.
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(student_marks)
    
    for name, lst_scores in student_marks.items():
        #print(name, lst_scores)
        ave_score = (sum(lst_scores)/len(lst_scores))
        student_marks[name] = ave_score

    print(f"{student_marks[query_name]:.2f}")
    
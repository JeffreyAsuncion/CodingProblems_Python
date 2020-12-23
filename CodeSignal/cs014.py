"""
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

Example

For a = [50, 60, 60, 45, 70], the output should be
alternatingSums(a) = [180, 105].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 105,
45 ≤ a[i] ≤ 100.

[output] array.integer
"""
def alternatingSums(a):
    if len(a) == 1:
        return [a[0], 0]
    if a == []:
        return [ 0, 0]
    one = 0
    two = 0
    for i in range(len(a)):
        if i % 2 == 0:
            one += a[i]
            print(1, a[i])
        else:
            two += a[i]
            print(2, a[i])
    return [one, two]  


a = [50, 60, 60, 45, 70]
print(alternatingSums(a))# = [180, 105]


"""
We have two monkeys, a and b, 
and the parameters a_smile and b_smile indicate 
if each is smiling. 
We are in trouble if they are both smiling or if neither of them is smiling. 
Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""


def monkey_trouble(a_smile, b_smile):

    # if both smile or both no smile return we in Trouble True
    if (a_smile == b_smile):
        return True
    else:
        return False




print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False)) 

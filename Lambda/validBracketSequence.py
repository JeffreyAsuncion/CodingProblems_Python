"""
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
Example

For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string sequence

A bracket sequence, consisting of the characters (, ), [, ], {, and }.

Guaranteed constraints:
0 ≤ sequence.length ≤ 106.

[output] boolean

true if sequence is a valid bracket sequence and false otherwise.
"""

def validBracketSequence(sequence):

    # stack for storing opening brackets
    stack = []

    # Loop for checking string 
    for char in sequence:
        # if its opening bracket, so push it in the 
        # stack
        if char == '{' or char == '(' or char == '[':
            stack.append(char) # push
        # else if its closing bracket then
        # check if the stack is empty then return false or
        # pop the top most element from the stack
        # and compare it
        elif char == '}' or char == ')' or char == ']':
            if len(stack) == 0:
                return False
            top_element = stack.pop() # pop
            # function to compare whether two 
            # brackets are corresponding to each other
            if not Compare(top_element, char):
                return False
    # lastly, check that stack is empty or not  
    if len(stack) != 0:
        return False
              
    return True

# Function to check two corresponding brackets
# equal or not. 
def Compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True  
    return False


"""
https://www.educative.io/edpresso/balanced-brackets-in-python
"""

sequence = "()"
print(validBracketSequence(sequence))# = true;
sequence = "()[]{}"
print(validBracketSequence(sequence))# = true;
sequence = "(]"
print(validBracketSequence(sequence))# = false;
sequence = "([)]"
print(validBracketSequence(sequence))# = false;
sequence = "{[]}"
print(validBracketSequence(sequence))# = true.
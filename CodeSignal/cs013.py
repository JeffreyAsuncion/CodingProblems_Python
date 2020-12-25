"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""

def reverseInParentheses(inputString):
    char = list(inputString)
    
    #stack
    open_bracket = []
    
    for i, c in enumerate(inputString):
        if c == '(':
            open_bracket.append(i)
        elif c == ')':
            j = open_bracket.pop()
            char[j:i] = char[i:j:-1]

    # review this stuff        
    return ''.join(c for c in char if c not in '()')



inputString = "(bar)"
print(reverseInParentheses(inputString))# = "rab";
inputString = "foo(bar)baz"
print(reverseInParentheses(inputString))# = "foorabbaz";
inputString = "foo(bar)baz(blim)"
print(reverseInParentheses(inputString))# = "foorabbazmilb";
inputString = "foo(bar(baz))blim"
print(reverseInParentheses(inputString))# = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

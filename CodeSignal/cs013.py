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
    for index, elem in enumerate(inputString):
        if elem == '(':
            start = index
        if elem == ')':
            end = index
    results = inputString[start:end + 1]
    front = inputString[:start]
    end = inputString[end+1:]
    mid = results.strip('(').strip(')')
    results = front + mid[::-1] + end
    return results



inputString = "(bar)"
print(reverseInParentheses(inputString))# = "rab";
inputString = "foo(bar)baz"
print(reverseInParentheses(inputString))# = "foorabbaz";
inputString = "foo(bar)baz(blim)"
print(reverseInParentheses(inputString))# = "foorabbazmilb";
inputString = "foo(bar(baz))blim"
print(reverseInParentheses(inputString))# = "foobazrabblim".
# Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".

"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""

def addBorder(picture):
    height = len(picture)
    width = len(picture[0])
    new_picture = []

    new_picture.append("*" * (width+2))
    for i in range(len(picture)):
        new_picture.append('*' + picture[i] + '*')
    new_picture.append("*" * (width+2))
    
    return new_picture

picture = ["abc",
           "ded"]
print(addBorder(picture))
                    #  = ["*****",
                    #   "*abc*",
                    #   "*ded*",
                    #   "*****"]
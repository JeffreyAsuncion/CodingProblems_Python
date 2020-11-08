"""
You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:

&& → and
|| → or
Both && and || should have a space " " on both sides.
"""
import re

if __name__ == '__main__':
    # inputs list of students in a list
    
    processedTxt = []
    for _ in range(int(input())):
        str1 = input()
        str1 = str1.replace(" && ", " and ").replace(" || ", " or ")
        
        #str_cleaned1 = re.sub(('&&'), 'and', str1)
        #str_cleaned2 = re.sub(('||'), 'or', str_cleaned1)
        
        processedTxt.append(str1)
    for txt in processedTxt:
        print(txt)
    
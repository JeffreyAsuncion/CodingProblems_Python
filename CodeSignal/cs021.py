"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.

There is no first number.
"""

import re

def isIPv4Address(inputString):
    
        
    
    # Make a regular expression
    # for validating an Ip-address
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
 
 
     
    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, inputString)): 
        return True
         
    else: 
        return False


inputString = "172.16.254.1"
print(isIPv4Address(inputString))# = true;

inputString = "172.316.254.1"
print(isIPv4Address(inputString))# = false.

#316 is not in range [0, 255].

inputString = ".254.255.0"
print(isIPv4Address(inputString))# = false.


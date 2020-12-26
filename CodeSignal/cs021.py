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

def isIPv4Address(inputString):
    if inputString[0] == '.' or inputString[-1] == '.' or len(inputString) < 4:
        return False

    new_str = inputString.split('.')
    
    checkNotNumber = [num for num in new_str]
    for num in checkNotNumber:
        if not num.isnumeric() :
            return False    

    new_str = [int(num) for num in new_str]
    for num in new_str:
        if num >= 0 or num <= 255:
            return True
    return False


inputString = "172.16.254.1"
print(isIPv4Address(inputString))# = true;

inputString = "172.316.254.1"
print(isIPv4Address(inputString))# = false.

#316 is not in range [0, 255].

inputString = ".254.255.0"
print(isIPv4Address(inputString))# = false.


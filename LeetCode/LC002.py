"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # this is old school math additional one column addition and carry 
        # carry value to next column tens column and hundreds and so on 
        # this repetition calls on the a recursive call

        # add the ones column with a c as the carry 
        val = l1.val + l2.val + c
        # calculate the next c Carry for the next recursion call
        c = val // 10

        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            # if l1 is shorter fill with 0
            if l1.next == None:
                l1.next = ListNode(0)
            # if l2 is shorter fill with 0
            if l2.next == None:
                l2.next = ListNode(0)
            # call the next recusion to calculate the next column, tens, then hundreds, then thousands
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        
        # all columns have been added
        # return results linked list ret
        return ret



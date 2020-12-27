"""
Note: Your solution should have O(n) time complexity, 
where n is the number of elements in l, and O(1) additional space complexity, 
since this is what you would be asked to accomplish in an interview.

Given a linked list l, 
reverse its nodes k at a time and 
return the modified list. 
k is a positive integer that is less than or equal to the length of l. 
If the number of nodes in the linked list is not a multiple of k, 
then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example
For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
1 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] integer k

The size of the groups of nodes that need to be reversed.

Guaranteed constraints:
1 ≤ k ≤ l size.

[output] linkedlist.integer

The initial list, with reversed groups of k elements.
"""
# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, value):
    self.value = value
    self.next = None


"""RecursionError: maximum recursion depth exceeded in comparison"""
# def reverseNodesInKGroups(l, k):
#     # keep track of a current node
#     current_node = l

#     # move (k nodes) nodes across to see if our sub-list size would be long enough
#     # iterate over a range of k
#     for i in range(k):
#         # check if we run out of nodes
#         if not current_node:
#             # just return l
#             return l
#         # increment our current node pointer/ref
#         current_node = current_node.next

#     # set a reveral ref to l
#     rev = l
#     # set current to l.next
#     current_node = l.next

#     # swap the next k elements
#     # iterate to k - 1
#     for i in range(k - 1):
#         # set current next to reversal
#         current_node.next = rev
#         # set current to current next (increment current)
#         current_node = current_node.next
#         # set my reversal to the current
#         rev = current_node

#     # recursive call
#     # connect the head node with the rest of the reversed sub lists
#     l.next = reverseNodesInKGroups(current_node,k)

#     #return our reversal
#     return ListNode(0)


"""new Solution"""

# some sort of helper function
def reverse(start, end):
    """
    takes in 2 nodes a start and end
    swaps all nodes
    iterating over start to end
    """
    
    # set a prev to the end
    prev = end
    # set a next_starting_node to the start.next
    next_starting_node = start.next
    # set a current_node
    current_node = start.next

    # while the current_node is not the end
    while current_node != end:
        # swap things
        # set a temp to current nodes next
        temp = current_node.next
        # set current nodes next to prev
        current_node.next = prev
        # set prev to current node
        prev = current_node
        # set current node to temp
        current_node = temp

    # set our starting node next to prev
    start.next = prev

    # return our next starting node to the caller
    return next_starting_node


def reverseNodesInKGroups(l,k):
    # check base case and end cases
    
    # if l is none
    # of if l.next is none
    # or if k == l
    if l is None or l.next is None or k==1:
        # return l
        return l
    
    # edge case to swap the first item (create a new list)
    list = ListNode(0) # just a placeholder / temporary head
    
    # apppend list l to the end of this list
    list.next = l
    
    # set list to the head
    starting_node = list

    # keep track of some counter
    counter = 0

    # iterate over the whole list
    while l:
        # increment my counter
        counter +=1

        # check if counter mod k is zero
        if counter % k == 0:  # for each k group    
            # set starting node to rev of starting node and l.next
            # (call to helper function)
            starting_node = reverse(starting_node, l.next) 
            
            # set l (the head) to the starting nodes next
            l = starting_node.next
        # otherwise, 
        else:
            # traverse forward setting l to l.next
            l = l.next
    # return the list.next    
    return list.next




    #  
    pass


def print_list(l):
    current_node = l
    while current_node:
        print(current_node.value, end="->")
        current_node = current_node.next
    print()
# set up a Linked List

n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)
n1.next.next.next = ListNode(4)
n1.next.next.next.next = ListNode(5)
n1.next.next.next.next.next = ListNode(6)
n1.next.next.next.next.next.next = ListNode(7)
n1.next.next.next.next.next.next.next = ListNode(8)
n1.next.next.next.next.next.next.next.next = ListNode(9)
n1.next.next.next.next.next.next.next.next.next = ListNode(10)
n1.next.next.next.next.next.next.next.next.next.next = ListNode(11)

print_list(n1)
print('------')
rev_list_head = reverseNodesInKGroups(n1, 3)
print_list(rev_list_head)
"""
Note: Your solution should have O(n) time complexity, 
where n is the number of elements in l, 
since this is what you will be asked to accomplish in an interview.

You have a singly linked list l, 
which is sorted in strictly increasing order, and an integer value. 
Add value to the list l, preserving its original sorting.

Note: in examples below and tests preview linked lists 
are presented as arrays just for simplicity of visualization: 
in real data you will be given a head node l of the linked list

Example

For l = [1, 3, 4, 6] and value = 5, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 5, 6];

For l = [1, 3, 4, 6] and value = 10, the output should be
insertValueIntoSortedLinkedList(l, value) = [1, 3, 4, 6, 10];

For l = [1, 3, 4, 6] and value = 0, the output should be
insertValueIntoSortedLinkedList(l, value) = [0, 1, 3, 4, 6].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers sorted in strictly increasing order. Thus, all integers in the list are pairwise distinct.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] integer value

A single integer value to be inserted into l. It is guaranteed that there is not an element equal to value in l before the insertion is performed.

Guaranteed constraints:
-109 ≤ value ≤ 109.

[output] linkedlist.integer

Return l after inserting value into it, with the original sorting preserved.
"""

# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, data=None):
      self.data = data
      self.next = None

class linked_list:
    def __init__(self):
        self.head = ListNode()
     
    def append(self, data):
        if self.head is None:
            self.head = ListNode(data) # next was head
            return 
        new_node = ListNode(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def sortedInsert(self, new_node): 
          
        # Special case for the empty linked list  
        if self.head is None: 
            new_node.next = self.head 
            self.head = new_node 
  
        else : 
            # Locate the node before the point of insertion 
            current = self.head 
            while(current.next is not None and
                 current.next.data < new_node.data): 
                current = current.next
              
            new_node.next = current.next
            current.next = new_node 

def insertValueIntoSortedLinkedList(l, value):

    llist = linked_list()
    for num in l:
        llist.append(num)
    new_node = ListNode(value)
    llist.sortedInsert(new_node)
    llist.display()
"""
# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def insertValueIntoSortedLinkedList(l, value):
    currentNode = l
    while currentNode != None:
        if currentNode.next == None:
            currentNode.next = ListNode(value)
            return l
        currentNode = currentNode.next
"""




l = [1, 3, 4, 6]
value = 5
insertValueIntoSortedLinkedList(l, value) # = [1, 3, 4, 5, 6];

l = [1, 3, 4, 6]
value = 10
insertValueIntoSortedLinkedList(l, value) # = [1, 3, 4, 6, 10];

l = [1, 3, 4, 6]
value = 0
insertValueIntoSortedLinkedList(l, value) # = [0, 1, 3, 4, 6].

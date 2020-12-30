"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.
As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.
The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        # Your code here
        # stack for inward 'self.in_stack' / 'bob'
        self.in_stack = Stack()
        # stack fo outward 'self.out_stack' / 'dave'
        self.out_stack = Stack()
        
    def enqueue(self, item):
        # Your code here
        # FIFO - O(1)
        # push item onto in stack
        self.in_stack.push(item)

    def dequeue(self):
        # Your code here
        # FIFO - O(n) - linear
        # check if the out_stack is empty
        if len(self.out_stack.data) == 0:
            # move items from in_stack to out_stack, reversing the order
            while len(self.in_stack.data) > 0:
                # pop out top item with the newest data
                newest_data = self.in_stack.pop()
                # push out newest data on to the out_stack
                self.out_stack.push(newest_data)

            # if our out_stack is still empty, raise an error
            if len(self.out_stack.data) == 0:
                raise IndexError("Can not dequeue from an empty queue!")

        # return the top of our stack
        return self.out_stack.pop()
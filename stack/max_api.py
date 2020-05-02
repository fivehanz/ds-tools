"""
EPI: Q8.1: Design a stack that includes a max operation, in addition to push and pop. 
The max method should return maximum value stored in the stack.

Implement Stack with max():return max element.
"""


class Stack:
    from collections import namedtuple
    maxCached = namedtuple('maxCache', ('element', 'max'))

    def __init__(self):
        self.elements = []

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self.elements.pop().element

    def push(self, elem):
        """
        Append namedtuple maxCached(elem, max) to elements
        """

        self.elements.append(
            self.maxCached(elem, elem if self.empty()
                           else max(elem, self.max()))
        )

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self.elements[-1].max

    def empty(self):
        return self.elements == []


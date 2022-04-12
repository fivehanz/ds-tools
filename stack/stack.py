"""
Stack
"""


class Stack:
    def __init__(self):
        self.Items = []

    def push(self, item):
        self.Items.append(item)

    def pop(self):
        return self.Items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.Items[-1]

    def isEmpty(self):
        return self.Items == []

    def getStack(self):
        return self.Items


# st = Stack()
# st.push(1)
# st.push("TWO")
# st.push(5)
# st.push("NINE")
# st.push("J")
# print(st.getStack())
# st.pop()
# st.pop()
# print(st.getStack())
# st.push("A")
# print(st.peek())

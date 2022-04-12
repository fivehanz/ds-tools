"""
(Singly) Linked List

Add/Remove first element: O(1)

"""


class Node:
    def __init__(self, item=None):
        self.item = item  # data item
        self.next = None  # pointer to successor


# wrapper for Nodes
class LinkedList:
    def __init__(self):
        self.head = Node()

    # Inserts at end
    def append(self, item):
        itr = self.head
        if itr.item is None:
            itr.item = item
        else:
            while True:
                if itr.next is None:
                    break
                itr = itr.next
            itr.next = Node(item)

    def removeAtFront(self):
        # check if head is Null
        if self.head is None:
            return
        # check if next Node exists
        elif self.head.next is None:
            self.head = None
        # set current head as next Node
        else:
            self.head = self.head.next

    def removeAtEnd(self):
        itr = self.head
        if itr.item is None:
            return
        else:
            while True:
                # check if last node is None from the previous Node
                if itr.next.next is None:
                    break
                itr = itr.next
            # set previous Node to the last Node as None
            itr.next = None

    def insertAtFront(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            head = self.head
            self.head = Node(item)
            self.head.next = head

    def insert(self, item, index=0):
        if index > self.length():
            print("Index is out of range")
            return None

        if index == 0: return self.insertAtFront(item)

        c_index, itr = 0, self.head
        while True:
            if c_index == index:
                previousNode.next = Node(item)
                previousNode.next.next = itr
                break
            previousNode = itr
            itr = itr.next
            c_index += 1

    def remove(self, index=0):
        if index >= self.length():
            print("Index is out of range")
            return None

        if index == 0: return self.removeAtFront()

        c_index, itr = 0, self.head
        while True:
            if c_index == index:
                previousNode.next = itr.next
                return
            previousNode = itr
            itr = itr.next

            c_index += 1

    def insertList(self, iList):
        pass

    def search(self, item):
        pass

    def printNodes(self):
        out = []
        itr = self.head
        while True:
            if itr.next is None:
                out.append(itr.item)
                break
            else:
                out.append(itr.item)
                itr = itr.next
        print(out)

    def length(self):
        itr, count = self.head, 1
        while True:
            # check if last node.next is None
            if itr.next is None:
                break
            count += 1
            itr = itr.next
        return count

    def get(self, i):
        if i >= self.length():
            print("Index is out of range")
            return None
        current_index = 0
        itr = self.head
        while True:
            if current_index is i: return itr.item
            current_index += 1
            itr = itr.next


"""

ll = LinkedList()

ll.append("H")
ll.append(2)
ll.insertAtFront("Front")

ll.printNodes(), print()

ll.insertAtFront("RemoveMe")

ll.printNodes(), print()

ll.removeAtEnd()

ll.printNodes(), print()

ll.append(3)
ll.append(4)

ll.insertAtFront("Front 2")

ll.printNodes(), print()

ll.removeAtEnd()

ll.append("Mon")

ll.printNodes(), print()

print(ll.length())

print(ll.get(ll.length()-1))

ll.insert("Zaynab")
ll.insert("Z", 5)

ll.printNodes(), print()

ll.remove(6)

ll.printNodes(), print()

"""

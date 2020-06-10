class Node:
    def __init__(self, item=None):
        self.next = None
        self.item = item


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, item = None):
        """ Insert an item at the begining of List """
        if self.head is None:
            self.head = Node(item)
        else:
            tmp = Node(item)
            tmp.next = self.head
            self.head = tmp


    def insertAtEnd(self, item = None):
        if self.head is None:
            self.head = Node(item)
        else:
            while(True):
                if self.head.next == None:
                    self.head.next = Node(item)
                    break
                self.head = self.head.next 
                


    def insert(self, index):
        pass

    def createWithArray(self):
        pass

    def display(self):
        while(self.head.next != None):
            print(self.head.item , end=" ")
            self.head = self.head.next
        

    def displayRecursive(self):
        pass

    def count(self):
        while(self.head.next != None):
            count += 1
            self.head = self.head.next
        return count


    def countRecursive(self):
        pass

    def max(self):
        pass

    def maxRecursive(self):
        pass

    def min(self):
        pass

    def minRecursive(self):
        pass

    def search(self):
        pass

    def searchRecursive(self):
        pass

    def betterSearch(self):
        """ Move the item to head """
        pass

    def deleteFirst(self):
        pass

    def deleteEnd(self):
        pass

    def delete(self, index):
        pass









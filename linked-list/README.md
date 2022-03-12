# linkedlist

- There are only two ways to store data, i.e. continous and non-continous. LinkedList is the non-continous way to store data in the memory.
- Every element must point to the next element.
- adding and deleting an element is O(1) time operation as oposed to O(n) in an Array.

## Singly LinkedList
- every node points to the next node. 

```go

type Node struct {
	val int 
        next *Node
}

type LinkedList struct {
	head *Node
        tail *Node
	len int        
}

```

## Doubly LinkedList
- doubly linked list consists two references, i.e. next node and previous node

```go

type Node struct {
	val int
        prev *Node
        next *Node
}

```

## Circular LinkedList
- the last node points to the first node forming a circle.

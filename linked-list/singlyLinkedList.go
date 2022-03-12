package singlyLinkedList

type Node struct {
	val  int
	next *Node
}

type LinkedList struct {
	head *Node
	tail *Node
	len  int
}

/* append an element at the end */
func (l *LinkedList) append(val int) {
	itr := l.head

}

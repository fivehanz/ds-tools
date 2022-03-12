package singlyLinkedList

type Node struct {
	val  int
	next *Node
}

type LinkedList struct {
	head *Node
	tail *Node
	size int
}

func (l *LinkedList) append(val int) {
	itr := l.head

}

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class MyLinkedList:

    def __init__(self):
        self.node = None
        self.lenth = 0

    def get(self, index: int) -> int:
        node = self.node
        i = 0
        while node:
            if index == i:
                return node.val
            i += 1
            node = node.next
        return -1

    def addAtHead(self, val: int) -> None:
        if self.node is None:
            node = Node(val)
            self.node = node
            self.lenth += 1
            return
        node = Node(val)
        node.next = self.node
        self.node = node
        self.lenth += 1

    def addAtTail(self, val: int) -> None:
        if self.node is None:
            node = Node(val)
            self.node = node
            self.lenth += 1
            return
        node = self.node
        while node.next is not None:
            node = node.next
        new_node = Node(val)
        node.next = new_node
        self.lenth += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if self.lenth < index or index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        i, node = 1, self.node
        while index != i and node.next is not None:
            node = node.next
            i += 1
        new_node = Node(val)
        new_node.next = node.next
        node.next = new_node
        self.lenth += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.lenth <= index or index < 0:
            return
        if index == 0:
            self.node = self.node.next
            self.lenth -= 1
            return
        node = self.node
        for _ in range(index):
            prev_node, node = node, node.next
        prev_node.next = node.next
        self.lenth -= 1

    def traverse_list(self, node=None):
        if node is None:
            node = self.node
        while node:
            print(node.val, end=" ")
            node = node.next
        print()


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(9)
obj.get(1)
obj.addAtIndex(1, 1)
obj.addAtIndex(1, 7)
obj.deleteAtIndex(1)
obj.addAtHead(7)
obj.addAtHead(4)
obj.deleteAtIndex(1)
obj.addAtIndex(1, 4)
obj.addAtHead(2)
obj.deleteAtIndex(5)
obj.traverse_list()

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("item not in the liat")
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                n.prev = new_node

    def traverse_list(self):
        if self.start_node is Node:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.data, " ")
                n = n.next

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def delete_element_by_value(self, x):
        if self.start_node.next is None:
            print("The list has no element to delete")
            return
        if self.start_node.next is None:
            if self.start_node.data == x:
                self.start_node = None
            else:
                print("Item not found")
            return

        if self.start_node.data == x:
            self.start_node = self.start_node.next
            self.start_node.prev = None
            return

        n = self.start_node
        while n.next is not None:
            if n.data == x:
                break
            n = n.next
            if n.next is not None:
                n.prev.next = n.next
                n.next.prev = n.prev
            else:
                if n.item == x:
                    n.prev.next = None
                else:
                    print("Element not found")

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        p = self.start_node
        q = p.next
        p.next = None
        p.prev = q
        while q is not None:
            q.prev = q.next
            q.next = p
            p = q
            q = q.next
        self.start_node = p


new_linked_list = DoublyLinkedList()
# new_linked_list.insert_in_emptylist(50)
new_linked_list.insert_at_start(10)
new_linked_list.insert_at_start(5)
# new_linked_list.insert_at_start(18)
new_linked_list.traverse_list()

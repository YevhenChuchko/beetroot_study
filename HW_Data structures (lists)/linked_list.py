class Node:
    def __init__(self, _id, value):
        self.id = _id
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node {self.id}: value {self.value}"


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def __iter__(self):
        self._current = self.head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            current_node = self._current
            self._current = self._current.next
            return current_node

    def add_node(self, value):
        _id = len(self) + 1
        new_node = Node(_id, value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_node_by_id(self, _id):
        current = self.head
        while current:
            if current.id == _id:
                return current
            current = current.next
        return None

    def remove_last_node(self):
        if not self.head:
            return None
        if not self.head.next:
            removed_node = self.head
            self.head = None
            return removed_node
        current = self.head
        while current.next and current.next.next:
            current = current.next
        removed_node = current.next
        current.next = None
        return removed_node

    def print_nodes(self):
        current = self.head
        while current:
            print(current)
            current = current.next


if __name__ == "__main__":
    container = LinkedList()
    container.add_node(10)
    container.add_node(20)
    container.add_node(30)
    print(len(container))
    container.print_nodes()


    print("\nПошук вузла за id:")
    node = container.find_node_by_id(2)
    if node:
        print(node)
    else:
        print("Node not found")


    print("\nВидалення останнього вузла:")
    removed_node = container.remove_last_node()
    if removed_node:
        print(f"Removed {removed_node}")
    else:
        print("Nothing to remove")

    print("\nСписок після видалення останнього вузла:")
    container.print_nodes()

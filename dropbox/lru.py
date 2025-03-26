class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = set()
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def display(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.value)
            curr = curr.next
        print(None)

    def access(self, value: int):
        if value in self.cache:
            curr = self.head.next
            while curr != self.tail:
                if curr.value == value:
                    self._remove(curr)
                    break
                curr = curr.next
        else:
            if len(self.cache) >= self.capacity:
                curr = self.tail.prev
                self._remove(curr)
                self.cache.remove(curr.value)

        self.cache.add(value)
        self._add(Node(value))

def main():
    cache = LRUCache(4)

    # Access integers
    cache.access(1)
    cache.access(2)
    cache.display()
    cache.access(3)
    cache.access(4)
    cache.display()  # Output: 4 -> 3 -> 2 -> 1 -> None

    # Accessing "2" makes it MRU
    cache.access(2)
    cache.display()  # Output: 2 -> 4 -> 3 -> 1 -> None

    # Adding a new integer evicts LRU (1)
    cache.access(5)
    cache.access(6)
    cache.display()


main()

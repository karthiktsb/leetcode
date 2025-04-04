class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def add(self, key):
        node = ListNode(key)
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove(self, key):
        node = self.head
        while node:
            if node.val == key:
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(key)
            self.add(key)
            return self.cache[key]
        else:
            return None

    def put(self, key: int, value: int) -> None:
        if self.count == self.capacity:
            self.cache.pop(self.tail.prev.val)
            self.remove(self.tail.prev.val)
            self.add(key)
            self.cache[key] = value
            self.count += 1
        else:
            self.add(key)
            self.cache[key] = value
            self.count += 1

    def display(self):
        print(self.cache.items())

def main():
    lru = LRUCache(2)

    lru.put(1, 10)
    lru.display()
    lru.get(1)
    lru.display()
    lru.put(2, 20)
    lru.display()
    lru.put(3, 30)
    lru.display()
    lru.get(2)
    lru.get(1);


main()


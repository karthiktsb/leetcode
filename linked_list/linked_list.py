from list_node import ListNode


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head:
            node = self.head
            while node.next:
                node = node.next
            node.next = ListNode(value)
        else:
            self.head = ListNode(value)

    def display(self):
        if self.head:
            node = self.head
            while node:
                print(node.value)
                node = node.next
        else:
            print("Empty List")


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.display()

    my_list.append(5)
    my_list.append(6)
    my_list.append(7)
    my_list.append(8)
    my_list.append(9)

    my_list.display()

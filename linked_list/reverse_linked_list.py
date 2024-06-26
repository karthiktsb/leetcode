from list_node import ListNode


def reverse(head: ListNode) -> ListNode:
    prev, current = None, head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev


if __name__ == '__main__':
    my_list = ListNode(5)
    my_list.next = ListNode(6)
    my_list.next.next = ListNode(7)
    my_list.next.next.next = ListNode(8)
    my_list.next.next.next.next = ListNode(9)

    node = my_list
    while node:
        print(node.value)
        node = node.next

    revers = reverse(my_list)

    print("--------")
    node = revers
    while node:
        print(node.value)
        node = node.next



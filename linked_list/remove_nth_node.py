from list_node import ListNode


def remove_nth_node(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    first, second = dummy, dummy
    count = 0

    for i in range(n + 1):
        if second:
            second = second.next
            count += 1

    if count == n + 1:
        while second:
            second = second.next
            first = first.next
        first.next = first.next.next
    else:
        raise Exception("n is bigger than size of linked list")

    return dummy.next


if __name__ == '__main__':
    my_list = ListNode(5)
    my_list.next = ListNode(6)
    my_list.next.next = ListNode(7)
    my_list.next.next.next = ListNode(8)
    my_list.next.next.next.next = ListNode(9)

    node1 = remove_nth_node(my_list, 5)
    while node1:
        print(node1.value)
        node1 = node1.next

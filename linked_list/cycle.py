from list_node import ListNode


def has_cycle(head: ListNode) -> bool:
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False


if __name__ == '__main__':
    my_list = ListNode(1)
    my_list.next = ListNode(2)
    my_list.next.next = ListNode(3)
    my_list.next.next.next = ListNode(4)
    my_list.next.next.next.next = ListNode(5)
    my_list.next.next.next.next.next = my_list
    #my_list.next.next.next.next.next.next = my_list.next

    print(has_cycle(my_list))
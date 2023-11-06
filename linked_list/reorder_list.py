from list_node import ListNode


def reorder_list(head: ListNode):
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    curr = slow
    prev = None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    first = head
    second = prev

    while second.next:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2

if __name__ == '__main__':
    my_list = ListNode(1)
    my_list.next = ListNode(2)
    my_list.next.next = ListNode(3)
    my_list.next.next.next = ListNode(4)
    my_list.next.next.next.next = ListNode(5)
    my_list.next.next.next.next.next = ListNode(6)

    reorder_list(my_list)

    node = my_list
    while node:
        print(node.value)
        node = node.next





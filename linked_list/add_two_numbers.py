from list_node import ListNode


def add_numbers(head1: ListNode, head2: ListNode) -> ListNode:
    node1 = head1
    node2 = head2
    result = ListNode(0)
    temp = result
    carry = 0

    while node1 or node2:
        if node1 and node2:
            summed = node1.value + node2.value + carry
            node1 = node1.next
            node2 = node2.next
        else:
            if node1:
                summed = node1.value + carry
                node1 = node1.next
            else:
                summed = node2.value + carry
                node2 = node2.next

        if summed > 9:
            carry = summed // 10
            summed = summed % 10
        else:
            carry = 0

        temp.next = ListNode(summed)
        temp = temp.next

    if carry:
        temp.next = ListNode(carry)

    return result.next


if __name__ == '__main__':
    my_list = ListNode(2)
    my_list.next = ListNode(4)
    my_list.next.next = ListNode(3)

    my_list1 = ListNode(5)
    my_list1.next = ListNode(6)
    my_list1.next.next = ListNode(4)

    res = add_numbers(my_list, my_list1)

    node = res
    while node:
        print(node.value)
        node = node.next

    my_list = ListNode(1)
    my_list.next = ListNode(2)
    my_list.next.next = ListNode(3)

    my_list1 = ListNode(4)
    my_list1.next = ListNode(5)
    my_list1.next.next = ListNode(6)

    res = add_numbers(my_list, my_list1)

    node = res
    while node:
        print(node.value)
        node = node.next



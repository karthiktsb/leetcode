from list_node import ListNode


def merge_list(head1: ListNode, head2: ListNode) -> ListNode:
    result, node1, node2 = None, head1, head2
    if node1 and node2:
        if node1.value <= node2.value:
            result = node1
            node1 = node1.next
        else:
            result = node2
            node2 = node2.next

        temp = result
        while node1 or node2:
            if node1 and node2:
                if node1.value <= node2.value:
                    temp.next = node1
                    node1 = node1.next
                else:
                    temp.next = node2
                    node2 = node2.next
            else:
                if node1:
                    temp.next = node1
                    node1 = node1.next
                else:
                    temp.next = node2
                    node2 = node2.next
            temp = temp.next
        return result
    else:
        if head1:
            return head1
        else:
            return head2


if __name__ == '__main__':
    my_list1 = ListNode(1)
    my_list1.next = ListNode(3)
    my_list1.next.next = ListNode(5)
    my_list1.next.next.next = ListNode(7)
    my_list1.next.next.next.next = ListNode(9)

    my_list2 = ListNode(2)
    my_list2.next = ListNode(4)
    my_list2.next.next = ListNode(6)
    my_list2.next.next.next = ListNode(8)
    my_list2.next.next.next.next = ListNode(10)

    merged = merge_list(my_list1, my_list2)

    node = merged
    while node:
        print(node.value)
        node = node.next
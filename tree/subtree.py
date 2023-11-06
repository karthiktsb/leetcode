from binary_tree import BinaryTree
from tree_node import TreeNode


def is_subtree(parent: TreeNode, child: TreeNode) -> TreeNode:
    subtree_head = TreeNode(0)

    def find_in_tree(node: TreeNode, val: int) -> bool:
        nonlocal subtree_head
        if node:
            if node.value == val:
                subtree_head = node
                return True
            else:
                return find_in_tree(node.left, val) or find_in_tree(node.right, val)
        else:
            return False

    def is_same_tree(a: TreeNode, b: TreeNode) -> bool:
        if a and b:
            return a.value == b.value and is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)
        else:
            if a or b:
                return False
            else:
                return True

    found = find_in_tree(parent, child.value)

    if found:
        return is_same_tree(subtree_head, child)
    else:
        return found


if __name__ == '__main__':
    my_tree = BinaryTree()

    my_list = [0, -1, 10, 15, -15, 9]

    for i in my_list:
        my_tree.add(i)

    node = my_tree.get_head()

    my_tree1 = TreeNode(10)
    my_tree1.right = TreeNode(15)
    my_tree1.left = TreeNode(9)

    print(is_subtree(my_tree.get_head(), my_tree1))
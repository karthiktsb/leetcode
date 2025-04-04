from binary_tree import BinaryTree
from tree_node import TreeNode


def is_valid_bst(node: TreeNode) -> bool:
    def valid(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False

        return valid(node.left, left, node.val) and valid(node.right, node.val, right)


    return valid(node, float("-inf"), float("inf"))


if __name__ == '__main__':
    my_tree = BinaryTree()

    my_list = [0, -1, 10, 15, -15, 9]

    for i in my_list:
        my_tree.add(i)

    node = my_tree.get_head()

    print(is_valid_bst(node))

    my_tree1 = TreeNode(0)
    my_tree1.right = TreeNode(-10)
    my_tree1.left = TreeNode(-20)

    print(is_valid_bst(my_tree1))

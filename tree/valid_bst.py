from binary_tree import BinaryTree
from tree_node import TreeNode


def is_valid_bst(node: TreeNode) -> bool:
    def dfs(curr: TreeNode):
        if curr:
            if (curr.left and curr.value < curr.left.value) or (curr.right and curr.value > curr.right.value):
                return False
            else:
                return dfs(curr.left) and dfs(curr.right)
        else:
            return True

    return dfs(node)


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

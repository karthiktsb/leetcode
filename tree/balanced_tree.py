from binary_tree import BinaryTree
from tree_node import TreeNode


def is_balanced(node: TreeNode):

    def dfs(node1: TreeNode):
        if node1:
            left = dfs(node1.left)
            right = dfs(node1.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(right, left) + 1
        else:
            return 0

    return dfs(node) != -1


if __name__ == '__main__':
    my_tree = BinaryTree()

    my_list = [0, -1, 10, 15, -15, 9, 19]

    for i in my_list:
        my_tree.add(i)

    node = my_tree.get_head()

    print(is_balanced(node))
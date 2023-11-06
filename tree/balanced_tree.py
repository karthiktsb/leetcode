from binary_tree import BinaryTree
from tree_node import TreeNode


def is_balanced(node: TreeNode):

    def dfs(curr: TreeNode):
        if curr:
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1
        else:
            return 0

    return dfs(node) != -1


if __name__ == '__main__':
    my_tree = BinaryTree()

    my_list = [0, -1, 10, 15, -15, 9]

    for i in my_list:
        my_tree.add(i)

    node = my_tree.get_head()

    print(is_balanced(node))
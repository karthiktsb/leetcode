from binary_tree import BinaryTree
from tree_node import TreeNode


def good_nodes(node: TreeNode):
    def dfs(curr: TreeNode, max_value: int):
        if curr:
            current = 1 if curr.value >= max_value else 0
            current_max = max(curr.value, max_value)
            return current + dfs(curr.left, current_max) + dfs(curr.right, current_max)
        else:
            return 0

    return dfs(node, node.value)


if __name__ == '__main__':
    my_tree = TreeNode(3)
    left1 = TreeNode(1)
    right1 = TreeNode(4)
    left2 = TreeNode(3)
    right2 = TreeNode(1)
    right3 = TreeNode(5)

    my_tree.left = left1
    my_tree.right = right1
    left1.left = left2
    right1.left = right2
    right1.right = right3

    node1 = my_tree

    print(good_nodes(node1))

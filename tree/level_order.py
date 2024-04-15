from binary_tree import BinaryTree
from tree_node import TreeNode
from collections import defaultdict


def level_order(node: TreeNode):
    result = defaultdict(list)

    def dfs(curr: TreeNode, level: int):
        if curr:
            result[level].append(curr.value)
            dfs(curr.left, level + 1)
            dfs(curr.right, level + 1)

    dfs(node, 0)
    return result.values()


if __name__ == '__main__':
    my_tree = BinaryTree()

    my_list = [0, -1, 10, 15, -15, 9]

    for i in my_list:
        my_tree.add(i)

    node1 = my_tree.get_head()

    print(level_order(node1))
from binary_tree import BinaryTree
from tree_node import TreeNode


def max_depth(node: TreeNode):
    def dfs(curr_node: TreeNode, depth: int):
        if curr_node:
            left_depth = dfs(curr_node.left, depth + 1)
            right_depth = dfs(curr_node.right, depth + 1)

            return max(depth, left_depth, right_depth)
        else:
            return 0

    return dfs(node, 0)


if __name__ == '__main__':
    my_tree = BinaryTree()

    my_list = [10, 5, 15, 3, 7, 12, 17, 0]

    for i in my_list:
        my_tree.add(i)

    node1 = my_tree.get_head()

    print(max_depth(node1))
from binary_tree import BinaryTree
from tree_node import TreeNode


def max_depth(node: TreeNode):
    def dfs(curr: TreeNode, depth: int):
        if curr:
            left = dfs(curr.left, depth + 1)
            right = dfs(curr.right, depth + 1)

            return max(depth, left, right)
        else:
            return 0

    return dfs(node, 0)

def max_depth1(node: TreeNode):
    max_depth = 0

    def dfs(curr: TreeNode, depth: int):
        nonlocal max_depth
        if curr:
            max_depth = max(depth, max_depth)
            dfs(curr.left, depth + 1)
            dfs(curr.right, depth + 1)
            return max_depth

    return dfs(node, 0)

if __name__ == '__main__':
    my_tree = BinaryTree()

    my_list = [10, 5, 15, 3, 7, 12, 17, 0]

    for i in my_list:
        my_tree.add(i)

    node1 = my_tree.get_head()

    print(max_depth(node1))
    print(max_depth1(node1))
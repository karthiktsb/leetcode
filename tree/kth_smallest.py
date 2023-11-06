from binary_tree import BinaryTree
from tree_node import TreeNode


def kth_smallest(node: TreeNode, k: int):
    result = []

    def dfs(node: TreeNode):
        if node:
            dfs(node.left)
            result.append(node.value)
            if len(result) >= k - 1:
                return
            dfs(node.right)

    dfs(node)

    if len(result) >= k - 1:
        return result[k - 1]
    else:
        return -1


if __name__ == '__main__':
    my_tree = BinaryTree()

    my_list = [10, 23, 14,22,44,33,22,44,22,22,44,5,6,7,7,5,5,4,4,3,3,3,5,5,6,6,5,4,5,6,6,4,4,1,2]

    for i in my_list:
        my_tree.add(i)

    node = my_tree.get_head()

    print(kth_smallest(node, 3))

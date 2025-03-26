from binary_tree import BinaryTree
from tree_node import TreeNode

def max_diameter(node: TreeNode):
    max_dia = 0

    def dfs(curr:TreeNode):
        nonlocal max_dia
        if curr:
            left = dfs(curr.left)
            right = dfs(curr.right)
            max_dia = max(left + right + 1, max_dia)

            return max(left, right)
        else:
            return 0

    dfs(node)
    return max_dia


if __name__ == '__main__':
    my_tree = BinaryTree()

    my_list = [0, -1, 10, 15, -15, 9]

    for i in my_list:
        my_tree.add(i)

    node = my_tree.get_head()
    #my_tree.display()

    print(max_diameter(node))

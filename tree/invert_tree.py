from binary_tree import BinaryTree
from tree_node import TreeNode


def invert_tree(head: TreeNode):
    def dfs(node: TreeNode):
        if node:
            dfs(node.left)
            dfs(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp

    dfs(head)


if __name__ == '__main__':
    my_binary_tree = BinaryTree()

    my_list = [10, 15, 25, 12, 20, 6, 8, 11, 3, 2, 1]

    for i in my_list:
        my_binary_tree.add(i)

    my_binary_tree.display()

    node = my_binary_tree.get_head()
    invert_tree(node)

    my_binary_tree.head = node

    print("--------")
    my_binary_tree.display()

from binary_tree import BinaryTree
from tree_node import TreeNode


def mirror_image(node: TreeNode):

    def dfs(curr: TreeNode):
        if curr:
            dfs(curr.left)
            dfs(curr.right)

            temp = curr.right
            curr.right = curr.left
            curr.left = temp

    dfs(node)


if __name__ == '__main__':
    my_binary_tree = BinaryTree()

    my_list = [10, 15, 25, 12, 20, 6, 8, 11, 3, 2, 1]

    for i in my_list:
        my_binary_tree.add(i)

    my_binary_tree.display()

    node = my_binary_tree.get_head()
    mirror_image(node)

    my_binary_tree.display()
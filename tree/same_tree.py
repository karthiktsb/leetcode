from binary_tree import BinaryTree
from tree_node import TreeNode


def is_same_tree(a: TreeNode, b:TreeNode) -> bool:
    def dfs(x: TreeNode, y: TreeNode):
        if x and y:
            if x.value == y.value:
                return  dfs(x.left, y.left) and dfs(x.right, y.right)
            else:
                return False
        else:
            if x or y:
                return False
            else:
                return True

    return dfs(a, b)


if __name__ == '__main__':
    my_tree1 = BinaryTree()

    my_list1 = [0, -1, 10, 15, -15, 9]

    for i in my_list1:
        my_tree1.add(i)

    node1 = my_tree1.get_head()

    my_tree2 = BinaryTree()

    my_list2 = [0, -1, 10, 15, -15, 91]

    for i in my_list2:
        my_tree2.add(i)

    node2 = my_tree2.get_head()

    print(is_same_tree(node1, node2))
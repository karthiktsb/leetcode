from binary_tree import BinaryTree
from tree_node import TreeNode


class btIterator:
    def __init__(self, head: TreeNode):
        self.stack = []
        self.left_dfs(head)

    def next(self):
        if not self.hasNext():
            raise Exception("No More Elements")

        node = self.stack.pop()

        if node.right:
            self.left_dfs(node.right)

        return node.value

    def hasNext(self):
        if self.stack:
            return True

    def left_dfs(self, curr):
        while curr:
            self.stack.append(curr)
            curr = curr.left


if __name__ == '__main__':
    my_binary_tree = BinaryTree()

    my_list = [10, 15, 25, 12, 20, 6, 8, 11, 3, 2, 1]

    for i in my_list:
        my_binary_tree.add(i)

    my_binary_tree.display()

    bti = btIterator(my_binary_tree.head)

    val = bti.next()
    while bti.hasNext():
        print(val)
        val = bti.next()
    print(val)

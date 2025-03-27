from binary_tree import BinaryTree
from tree_node import TreeNode


class btIterator:
    def __init__(self, head: TreeNode):
        self.stack = []
        self.left_dfs(head)

    def next(self):
        if not self.hasNext():
            return StopIteration()

        curr = self.stack.pop()

        if curr.right:
            self.left_dfs(curr.right)

        return curr.value


    def hasNext(self):
        if self.stack:
            return True
        else:
            return False

    def left_dfs(self, curr):
        if curr:
            self.stack.append(curr)
            self.left_dfs(curr.left)


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

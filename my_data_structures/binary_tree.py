from my_data_structures.tree_node import TreeNode


class BinaryTree:
    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head:
            node = self.head

            while node:
                if node.value == value:
                    break
                else:
                    if value > node.value:
                        if node.right:
                            node = node.right
                        else:
                            node.right = TreeNode(value)
                    else:
                        if node.left:
                            node = node.left
                        else:
                            node.left = TreeNode(value)
        else:
            self.head = TreeNode(value)

    def print(self):
        def dfs(node: TreeNode):
            if node:
                dfs(node.left)
                print(node.value)
                dfs(node.right)

        dfs(self.head)

    def load_list(self, input):
        for i in input:
            self.add(i)

    def find(self, value):
        if self.head:
            node = self.head

            while node:
                if node.value == value:
                    return True
                else:
                    if value > node.value:
                        node = node.right
                    else:
                        node = node.left
        return False


if __name__ == '__main__':
    bt = BinaryTree()

    bt.add(10)
    bt.add(5)
    bt.add(15)
    bt.add(25)
    bt.add(-5)

    print(bt.find(6))

    bt.load_list([34,45,65,34,4,545,345,434,234,24,4,4,54,43,34,343,234,234,234,4545,43232423,234,234,123,12313,13324,454])
    print(bt.find(454))
    bt.print()


    bt1 = BinaryTree()

    bt1.load_list([5,4,6,3,7])

    bt1.print()
    print(bt1.find(7))
    print(bt1.find(9))

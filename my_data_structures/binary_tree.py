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
                dfs(node.right)
                print(node.value)


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

    bt.add(1)
    bt.add(2)
    bt.add(3)
    bt.add(4)
    bt.add(5)
    bt.print()
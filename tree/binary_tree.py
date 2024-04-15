from tree_node import TreeNode


class BinaryTree:
    def __init__(self):
        self.head = None

    def add(self, value: int):
        if self.head:
            node = self.head
            while node:
                if node.value == value:
                    break

                if value > node.value:
                    if node.right:
                        node = node.right
                    else:
                        node.right = TreeNode(value)
                        break
                else:
                    if node.left:
                        node = node.left
                    else:
                        node.left = TreeNode(value)
                        break
        else:
            self.head = TreeNode(value)

    def display(self):
        def dfs(node):
            if node:
                dfs(node.right)
                print(node.value)
                dfs(node.left)

        dfs(self.head)

    def get_head(self):
        return self.head


if __name__ == '__main__':
    my_binary_tree = BinaryTree()

    my_list = [10, 15, 25, 12, 20, 6, 8, 11, 3, 2, 1]

    for i in my_list:
        my_binary_tree.add(i)

    my_binary_tree.display()

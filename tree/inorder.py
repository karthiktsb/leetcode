from tree_node import TreeNode


def buildTree(preorder: list[int], inorder: list[int]):
    if not inorder or not preorder:
        return None

    node = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    node.left = buildTree(preorder[1: mid + 1], inorder[:mid])
    node.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return node

def dfs(node: TreeNode):
    if node:
        dfs(node.left)
        print(node.value)
        dfs(node.right)


def main():
    root = buildTree([1,2,3,4], [2,1,3,4])
    dfs(root)


main()




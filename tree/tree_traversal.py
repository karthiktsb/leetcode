from tree_node import TreeNode
from collections import deque


def bfs(node: TreeNode):
    my_queue = deque()

    my_queue.append(node)

    while my_queue:
        curr = my_queue.popleft()

        print(curr.value)
        if curr.left:
            my_queue.append(curr.left)
        if curr.right:
            my_queue.append(curr.right)

# left -> root -> right
def dfs_in_order(node: TreeNode):
    if not node:
        return

    def dfs(curr: TreeNode):
        if curr:
            dfs(curr.left)
            print(curr.value)
            dfs(curr.right)

    dfs(node)


# root -> left -> right
def dfs_pre_order(node: TreeNode):
    if not node:
        return

    def dfs(curr: TreeNode):
        if curr:
            print(curr.value)
            dfs(curr.left)
            dfs(curr.right)

    dfs(node)


# left -> right -> root
def dfs_post_order(node: TreeNode):
    if not node:
        return

    def dfs(curr: TreeNode):
        if curr:
            dfs(curr.left)
            dfs(curr.right)
            print(curr.value)

    dfs(node)


def in_order_stack(node: TreeNode):
    if not node:
        return

    stack = deque()

    def stack_left(node):
        if node:
            stack.append(node)
            stack_left(node.left)

    stack_left(node)
    while stack:
        curr = stack.pop()
        print(curr.value)
        if curr.right:
            stack_left(curr.right)


def pre_order_stack(node: TreeNode):
    if not node:
        return

    stack = deque()

    stack.append(node)
    while stack:
        curr = stack.pop()
        print(curr.value)

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)


def reverse_in_order_order_stack(node: TreeNode):
    if not node:
        return

    stack = deque()

    def stack_right(node):
        if node:
            stack.append(node)
            stack_right(node.right)

    stack_right(node)
    while stack:
        curr = stack.pop()
        print(curr.value)
        if curr.left:
            stack_right(curr.left)


def post_order_stack(node: TreeNode):
    if not node:
        return

    stack1 = deque()
    stack2 = deque()
    stack1.append(node)

    while stack1:
        curr = stack1.pop()
        stack2.append(curr)

        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)

    while stack2:
        print(stack2.pop().value)


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(0)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)

    print("---breadth first traversal------")
    bfs(root)
    print("----in order recursion-----")
    dfs_in_order(root)
    print("----pre order recursion-----")
    dfs_pre_order(root)
    print("----post order recursion-----")
    dfs_post_order(root)
    print("----in order stack-----")
    print(in_order_stack(root))
    print("----pre order stack-----")
    print(pre_order_stack(root))
    print("----reverse in order stack-----")
    print(reverse_in_order_order_stack(root))
    print("----post order stack-----")
    print(post_order_stack(root))

main()



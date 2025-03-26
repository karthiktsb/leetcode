class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] > val:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            elem = self.stack.pop()
            if self.min_stack and self.min_stack[-1] == elem:
                self.min_stack.pop()
            return elem
        else:
            return None

    def top(self) -> int:
        if self.min_stack:
            self.min_stack[-1]


    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None



if __name__ == '__main__':
    min_stack = MinStack()

    min_stack.push(5)
    print(min_stack.getMin())
    min_stack.push(2)
    min_stack.push(3)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.getMin())

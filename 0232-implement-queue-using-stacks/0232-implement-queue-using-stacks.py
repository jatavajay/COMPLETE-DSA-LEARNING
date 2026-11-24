class MyQueue:

    def __init__(self):
        self.st_one = []
        self.st_two = []

    def push(self, x: int) -> None:
        self.st_one.append(x) 

    def pop(self) -> int:
        if not self.st_two:
            while self.st_one:
                top = self.st_one.pop()
                self.st_two.append(top)
        return self.st_two.pop()

    def peek(self) -> int:
        if not self.st_two:
            while self.st_one:
                self.st_two.append(self.st_one.pop())

        return self.st_two[-1]

    def empty(self) -> bool:
        return not self.st_one and not self.st_two


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
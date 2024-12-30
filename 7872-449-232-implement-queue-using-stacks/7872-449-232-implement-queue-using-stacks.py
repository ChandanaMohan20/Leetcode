class MyQueue:

    def __init__(self):
        #to push
        self.stackin = []

        #to pop/peek
        self.stackout = []

    def push(self, x: int) -> None:
        # to push element into the queue
        self.stackin.append(x)

    def pop(self) -> int:
        self. helper_transfer()
        return self.stackout.pop()

    def peek(self) -> int:
        self.helper_transfer()
        value = self.stackout[-1]
        return value

    def empty(self) -> bool:
        return not self.stackin and not self.stackout

    def helper_transfer(self):
        #adding elements to stckout when stackout is empty

        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
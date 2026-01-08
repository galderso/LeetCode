class MinStack(object):

    def __init__(self):
        self.stack = []
        self.smallest = []

    def push(self, val):
        self.stack.append(val)
        if not self.smallest or val <= self.smallest[-1]:
            self.smallest.append(val)

    def pop(self):
        if self.stack[-1] == self.smallest[-1]:
            self.smallest.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.smallest[-1]

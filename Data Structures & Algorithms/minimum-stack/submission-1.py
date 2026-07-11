class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            minimum_val = val
        else:
            previous_min=self.stack[-1][1]
            minimum_val = min(val,previous_min)
        self.stack.append((val,minimum_val))
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

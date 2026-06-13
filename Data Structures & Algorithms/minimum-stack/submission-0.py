class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.m:
            self.m.append(val)
        else:
            self.m.append(min(self.m[-1], val))

    def pop(self) -> None:
        self.m.pop(-1)
        return self.s.pop(-1)

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
        

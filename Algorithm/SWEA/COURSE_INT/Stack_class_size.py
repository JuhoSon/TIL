# stack 구현(크기를 고정시켜 구현)
class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.top = -1

    def is_empty(self):
        return False if (self.top != -1) else True

    def is_full(self):
        return True if (self.top == self.size-1) else False

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        else:
            self.top += 1
            self.items[self.top] = item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.items[self.top]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            value = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return value

    def __str__(self):
        result = '\n-----'
        for d in self.items:
            if d is None:
                result = f'\n| {d} |' + result
            else:
                result = f'\n|  {d}   |' + result
        return result
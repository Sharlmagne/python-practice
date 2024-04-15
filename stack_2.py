from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Stack Length:", stack.size())
    print("Peek:", stack.peek())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Stack Length:", stack.size())
    print(stack.is_empty())
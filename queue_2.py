from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        return self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def front(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    print("Front:", queue.front())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Queue Length:", queue.size())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Queue Length:", queue.size())
    print(queue.is_empty())
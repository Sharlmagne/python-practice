class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Stack:
    def __init__(self):
        self.bottom = None
        self.top = None
        self.length = 0

    def increase_length(self):
        self.length += 1

    def decrease_length(self):
        self.length -= 1

    def push(self, data):
        # Create new node as the head node
        node = Node(data, None, self.bottom)
        if self.bottom is None:
            self.bottom = node
            self.top = node
            self.increase_length()
        else:
            node = Node(data, None, self.bottom)
            self.top.next = node
            self.top.next.prev = self.top
            self.top = node
            self.increase_length()

    def pop(self):
        if self.is_empty():
            raise Exception("This stack is empty")

        pop_data = self.top.data
        if self.top.prev is not None:
            self.top.prev.next = None
            self.top = self.top.prev
        else:
            self.top = None
            self.bottom = None
        self.decrease_length()
        return pop_data

    def peek(self):
        return self.top.data

    def is_empty(self):
        if self.bottom is None:
            return True
        else:
            return False

    def iterate(self):
        # Check if linked list is empty
        node = self.bottom
        if self.is_empty():
            raise Exception("This stack is empty")

        # Append values to show
        node_values = "Stack: "

        # Print in reverse
        count = 0
        while count < self.length:
            node_value = str(node.data) + "<->"
            node_values += node_value
            node = node.next
            count += 1
        print(node_values)


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.iterate()
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    stack.iterate()
    print("Stack Length:", stack.length)
    print("Peek:", stack.peek())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Stack Length:", stack.length)


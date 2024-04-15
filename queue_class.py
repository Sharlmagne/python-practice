class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def increase_length(self):
        self.length += 1

    def decrease_length(self):
        self.length -= 1

    def enqueue(self, data):
        # Create new node as the head node
        node = Node(data, None, self.head)
        if self.head is None:
            self.head = node
            self.tail = node
            self.increase_length()
        else:
            self.head.prev = node
            self.head = node
            self.increase_length()

    def dequeue(self):
        if self.is_empty():
            raise Exception("This stack is empty")

        dequeue_data = self.tail.data
        if self.tail.prev is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.tail = None
            self.head = None

        self.decrease_length()
        return dequeue_data

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def iterate(self):
        # Check if linked list is empty
        if self.is_empty():
            raise Exception("This stack is empty")

        # Append values to show
        node_values = "Stack: "
        node = self.head
        count = 0
        while count < self.length:
            node_value = str(node.data) + "-->"
            node_values += node_value
            node = node.next
            count += 1
        print(node_values)

    def size(self):
        return self.length


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.iterate()
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Queue Length:", queue.size())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Queue Length:", queue.size())
    print(queue.is_empty())
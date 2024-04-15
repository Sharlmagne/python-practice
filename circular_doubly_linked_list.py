class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def increase_length(self):
        self.length += 1

    def decrease_length(self):
        self.length -= 1

    def reconnect_head_and_tail(self):
        self.tail.next = self.head
        self.head.prev = self.tail

    def insert_at_beg(self, data):
        # Create new node as the head node
        node = Node(data, None, self.head)

        if self.head is None:
            self.head = node
            self.tail = node
            self.reconnect_head_and_tail()
            self.increase_length()
            return

        if self.head is not None:
            # Connect new node to head
            node.next = self.head
            # Change head to new node
            self.head = node
            # Set second node previous to new head
            self.head.next.prev = self.head
            self.reconnect_head_and_tail()
            self.increase_length()
            return

    def insert_at_end(self, data):
        # Create new node
        node = Node(data, self.head)

        # If list is empty
        if self.head is None:
            self.head = node
            self.tail = node
            self.reconnect_head_and_tail()
            self.increase_length()
            return

        # If list is not empty
        if self.head is not None:
            # Connect old tail to new node
            self.tail.next = node
            # Set new node previous to old tail
            node.prev = self.tail
            # Set the new node as tail
            self.tail = node
            self.reconnect_head_and_tail()
            self.increase_length()
            return

    def remove_at_beg(self):
        # Change the head of the linked list to the second node
        self.head = self.head.next
        self.reconnect_head_and_tail()
        self.decrease_length()

    def remove_at_end(self):
        node = self.head
        count = 0
        length_of_list = self.length

        # Find the second to last item in the linked list
        while count < length_of_list - 2:
            node = node.next
            count += 1

        # Set as last node
        self.tail = node
        self.reconnect_head_and_tail()

        self.decrease_length()

    def insert_values(self, list_of_values):
        self.head = None
        for value in list_of_values:
            self.insert_at_end(value)

    def insert_at(self, data, index):
        # Check for invalid index
        if index < 0 or index >= self.length:
            raise Exception("Invalid Index")

        # Check if index is at the beginning
        if index == 0:
            self.insert_at_beg(data)
        else:
            node = self.head
            count = 0
            while count < self.length:
                if count == index - 1:
                    new_node = Node(data, node, node.next)
                    node.next.prev = new_node
                    node.next = new_node
                    break
                node = node.next
                count += 1
            self.increase_length()

    def remove_at(self, index):
        # Check for invalid index
        if index < 0 or index >= self.length:
            raise Exception("Invalid Index")

        # Check if index is at the end
        if index == self.length - 1:
            self.remove_at_end()
        # Check if index is at the beginning
        elif index == 0:
            self.remove_at_beg()
        else:
            node = self.head
            count = 0
            while count < self.length:
                if count == index - 1:
                    # Set the node ahead previous node to the current node.
                    node.next.next.prev = node
                    # Set the current node's next node to the next node's next node. 😅
                    node.next = node.next.next
                    break
                node = node.next
                count += 1
            self.decrease_length()

    def insert_after(self, data, new_data):
        node = self.head
        count = 0
        while count < self.length:
            # If search is in last node
            if node.data == data and count == self.length - 1:
                self.insert_at_end(new_data)
                break
            # Search for first occurrence of data_after value in linked list
            if node.data == data:
                # Insert new_data after current the data's node
                new_node = Node(new_data, node, node.next)
                node.next.prev = new_node
                node.next = new_node
                self.increase_length()
                break
            node = node.next

    def remove_by_value(self, data):
        node = self.head
        count = 0
        while count < self.length:
            # Remove first node that contains data
            if node.data == data:
                break
            node = node.next
            count += 1

        if node is not None and count > self.length:
            self.remove_at(count)
        else:
            print("Data not in Linked List")

    def traverse(self):
        # Check if linked list is empty
        node = self.head
        if node is None:
            print("Linked List is empty")
            return

        # Append values to show
        node_values = ""
        count = 0
        while count < self.length:
            node_value = str(node.data) + "<->"
            node_values += node_value
            node = node.next
            count += 1
        print(node_values)

    def reverse(self):
        # Check if linked list is empty
        node = self.head
        if node is None:
            print("Linked List is empty")
            return

        # Append values to show
        node_values = "Reversed Linked List: "

        count = 0
        # Go to the last node
        while count < self.length-1:
            node = node.next
            count += 1

        # Print in reverse
        count = 0
        while count < self.length:
            node_value = str(node.data) + "<->"
            node_values += node_value
            node = node.prev
            count += 1
        print(node_values)


if __name__ == "__main__":
    ll = CircularDoublyLinkedList()
    names = ["Bob", "Ben", "Lisa", "Maria", "Penny"]
    ll.insert_values(names)
    ll.traverse()
    ll.reverse()
    ll.insert_at("ShuShu", 4)
    ll.traverse()
    ll.reverse()
    ll.remove_at(2)
    ll.traverse()
    ll.reverse()
    ll.insert_after("ShuShu", "Sharl")
    ll.traverse()
    ll.reverse()
    ll.remove_by_value("Sharl")
    ll.traverse()
    ll.reverse()

    print()
    print(f"End Data: {ll.tail.data}")
    print(f"Head Data: {ll.head.data}")

    print(f"Head Prev Data: {ll.head.prev.data}")
    print(f"End Next Data: {ll.tail.next.data}")
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def increase_length(self):
        self.length += 1

    def decrease_length(self):
        self.length -= 1

    def insert_at_beg(self, data):
        # Create new node as the head node
        node = Node(data, self.head)
        self.head = node
        self.increase_length()

    def remove_at_beg(self):
        # Change the head of the linked list to the second node
        self.head = self.head.next
        self.decrease_length()

    def insert_at_end(self, data):
        # Check if linked list is empty
        if self.head is None:
            self.head = Node(data, None)
            self.increase_length()
            return

        # Cycle to the last node
        node = self.head
        while node.next is not None:
            node = node.next

        # Change the pointer of the last node to the new node
        node.next = Node(data, None)
        self.increase_length()

    def remove_at_end(self):
        node = self.head
        count = 0
        length_of_list = self.length

        # Find the second to last item in the linked list
        while count < length_of_list - 2:
            node = node.next
            count += 1
        node.next = None
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
            while node is not None:
                if count == index - 1:
                    node.next = Node(data, node.next)
                    self.increase_length()
                    break
                node = node.next
                count += 1

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
            while node is not None:
                if count == index - 1:
                    # Set the current node's next node to the next node's next node. 😅
                    node.next = node.next.next
                    self.decrease_length()
                    break
                node = node.next
                count += 1

    def insert_after(self, data, new_data):
        node = self.head
        while node is not None:
            # Search for first occurrence of data_after value in linked list
            if node.data == data:
                # Insert new_data after current the data's node
                new_node = Node(new_data, node.next)
                node.next = new_node
                self.increase_length()
                break
            node = node.next

    def remove_by_value(self, data):
        node = self.head
        count = 0
        while node is not None:
            # Remove first node that contains data
            if node.data == data:
                break
            node = node.next
            count += 1

        if node is not None:
            self.remove_at(count)
        else:
            print("Data not in Linked List")

    def print(self):
        # Check if linked list is empty
        node = self.head
        if node is None:
            print("Linked List is empty")
            return

        # Append values to show
        node_values = ""
        count = 0
        while count < self.length:
            node_value = str(node.data) + "-->"
            node_values += node_value
            node = node.next
            count += 1
        print(node_values)


if __name__ == "__main__":
    ll = LinkedList()
    names = ["Bob", "Ben", "Lisa", "Maria", "Penny"]
    ll.insert_values(names)
    ll.print()
    ll.insert_at("ShuShu", 4)
    # ll.remove_at(4)
    ll.print()

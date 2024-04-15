class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def add_child(self, data):
        # Check if the data is duplicated
        if data == self.data:
            return

        if data < self.data:
            # Check if leaf node
            if self.left_node:
                # Add a child to the left node
                self.left_node.add_child(data)
            else:
                # Create a new node
                self.left_node = BinarySearchTreeNode(data)
        else:
            # Check if leaf node
            if self.right_node:
                # Add a child to the left node
                self.right_node.add_child(data)
            else:
                # Create a new node
                self.right_node = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # Check for left node
        if self.left_node:
            # Recursively check for more left nodes and add the data to elements
            elements += self.left_node.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # Check for right node
        if self.right_node:
            # Recursively check for more right nodes and add the data to elements
            elements += self.right_node.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left_node:
            elements += self.left_node.pre_order_traversal()

        if self.right_node:
            elements += self.right_node.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left_node:
            elements += self.left_node.post_order_traversal()

        if self.right_node:
            elements += self.right_node.post_order_traversal()

        elements.append(self.data)

        return elements

    def search(self, val):
        # Check for value
        if self.data == val:
            return True

        # Check left node
        if val < self.data:
            if self.left_node:
                # If there is data in left node, recursively search that node
                return self.left_node.search(val)
            else:
                return False

        # Check right node
        if val > self.data:
            if self.right_node:
                # If there is data in right node, recursively search that node
                return self.right_node.search(val)
            else:
                return False

    def find_min(self):
        value = self.data
        if self.left_node:
            value = self.left_node.find_min()
        return value

    def find_max(self):
        value = self.data
        if self.right_node:
            value = self.right_node.find_max()
        return value

    def calculate_sum(self):
        if isinstance(self.data, (int, float)):
            return sum(self.in_order_traversal())
        else:
            return

    def delete(self, val):
        # Determine the side of the tree to search
        if val < self.data:
            if self.left_node:
                self.left_node = self.left_node.delete(val)
        elif val > self.data:
            if self.right_node:
                self.right_node = self.right_node.delete(val)
        else:
            # If current node is a leaf node
            if self.right_node is None and self.left_node is None:
                return None
            # If value only in right node
            if self.left_node is None:
                return self.right_node
            # If value only in left node
            if self.right_node is None:
                return self.left_node

            # # Use minimum value from the right subtree
            # min_val = self.right_node.find_min()
            # self.data = min_val
            # self.right_node = self.right_node.delete(min_val)

            # Use maximum value from the left subtree
            max_val = self.left_node.find_max()
            self.data = max_val
            self.left_node = self.left_node.delete(max_val)
        return self


# Helper function
def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers = [15, 12, 7, 14, 27, 20, 23, 88]
    # numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    countries = ["Jamaica", "England", "China", "USA", "Japan", "Canada"]
    tree = build_tree(numbers)
    print(f"In-Order Traversal: {tree.in_order_traversal()}")
    print(f"Pre-Order Traversal: {tree.pre_order_traversal()}")
    print(f"Post-Order Traversal: {tree.post_order_traversal()}")
    print(tree.search(117))
    print(tree.search(27))
    print(f"Sum of tree: {tree.calculate_sum()}")
    print(f"Min Node: {tree.find_min()}")
    print(f"Max Node: {tree.find_max()}")
    tree = build_tree(countries)
    print(tree.in_order_traversal())
    print(tree.search("Spain"))
    print(tree.search("Jamaica"))
    print(f"Min Node: {tree.find_min()}")
    print(f"Max Node: {tree.find_max()}")
    print(f"Sum of tree: {tree.calculate_sum()}")
    tree.delete("England")
    print(f"In-Order Traversal: {tree.in_order_traversal()}")

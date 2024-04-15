class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.level = 0

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        # Check and set the level of the node
        if self.parent:
            self.level = self.parent.level + 1

        # Add indentation and prefix to the children
        indentation = " " * self.level * 2
        prefix = "|__" if self.level else ""

        print(f"{indentation}{prefix}{self.data}")

        if self.children:
            for node in self.children:
                node.print_tree()


# Helper function
def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Pixel"))
    cellphone.add_child(TreeNode("Galaxy"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == "__main__":
    tree = build_tree()
    tree.print_tree()
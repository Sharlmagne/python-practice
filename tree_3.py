from tree import TreeNode


class TreeNodeLevel(TreeNode):

    def print_tree(self, level):
        # Check and set the level of the node
        if self.parent:
            self.level = self.parent.level + 1

        if self.level > level:
            return

        # Add indentation and prefix to the children
        indentation = " " * self.level * 2
        prefix = "|__" if self.level else ""

        print(f"{indentation}{prefix}{self.data}")

        if self.children:
            for node in self.children:
                node.print_tree(level)


# Helper function
def build_tree():
    root = TreeNodeLevel("Global")

    india = TreeNodeLevel("India")

    gujarat = TreeNodeLevel("Gujarat")
    gujarat.add_child(TreeNodeLevel("Ahmedabad"))
    gujarat.add_child(TreeNodeLevel("Baroda"))

    karnataka = TreeNodeLevel("Karnataka")
    karnataka.add_child(TreeNodeLevel("Bangluru"))
    karnataka.add_child(TreeNodeLevel("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNodeLevel("USA")

    nj = TreeNodeLevel("New Jersey")
    nj.add_child(TreeNodeLevel("Princeton"))
    nj.add_child(TreeNodeLevel("Trenton"))

    california = TreeNodeLevel("California")
    california.add_child(TreeNodeLevel("San Francisco"))
    california.add_child(TreeNodeLevel("Mountain View"))
    california.add_child(TreeNodeLevel("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == "__main__":
    tree = build_tree()
    print("Level 3")
    tree.print_tree(3)
    print("\nLevel 2")
    tree.print_tree(2)
    print("\nLevel 1")
    tree.print_tree(1)

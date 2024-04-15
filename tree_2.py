class TreeNode:
    def __init__(self, name, designation):
        self.data = (name, designation)
        # self.data = name
        self.children = []
        self.parent = None
        self.level = 0

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, option):
        option_results = f"{self.data[0]} {self.data[1]}"
        if option.lower() == "name":
            option_results = f"{self.data[0]}"
        if option.lower() == "designation":
            option_results = f"{self.data[1]}"

        # Check and set the level of the node
        if self.parent:
            self.level = self.parent.level + 1

        # Add indentation and prefix to the children
        indentation = " " * self.level * 2
        prefix = "|__" if self.level else ""

        print(f"{indentation}{prefix}{option_results}")

        if self.children:
            for node in self.children:
                node.print_tree(option)


# Helper funciton
def build_tree():
    root = TreeNode("John", "CEO")

    cto = TreeNode("Paul", "CTO")
    infrastructure_head = TreeNode("Dennis", "Infrastructure Head")
    infrastructure_head.add_child(TreeNode("Anna", "Cloud Manager"))
    infrastructure_head.add_child(TreeNode("Peter", "App Manager"))
    cto.add_child(infrastructure_head)
    cto.add_child(TreeNode("Craig", "Application Head"))

    hr_head = TreeNode("Donna", "HR Head")
    hr_head.add_child(TreeNode("Fiona", "Recruitment Manager"))
    hr_head.add_child(TreeNode("Desreen", "Policy Manager"))

    root.add_child(cto)
    root.add_child(hr_head)

    return root


if __name__ == "__main__":
    tree = build_tree()
    print("\nDesignation Only")
    tree.print_tree("designation")
    print("\nName Only")
    tree.print_tree("name")
    print("\nBoth name and designation")
    tree.print_tree("both")












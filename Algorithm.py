from Node import Node


class Algorithm:
    parent_set = []

    def __init__(self, parent_set):
        self.parent_set = parent_set

    def is_finished(self):
        for node in self.parent_set:
            if not node.is_connected():
                node.initially_unconnected = True
                return False
        return True

    def get_unconnected_parent(self):
        for node in self.parent_set:
            if not node.is_connected():
                return node

    def execute(self):
        print("Calculation Starts...\n")

        for node in self.parent_set:
            if not node.is_connected():
                node.initially_unconnected = True

        while not self.is_finished():
            current_parent_set = []
            current_child_set = []
            current_parent = self.get_unconnected_parent()
            current_child = current_parent.get_available_set()[0]

            current_parent_set.append(current_parent)
            current_child_set.append(current_child)

            while current_child.is_connected():
                current_parent = current_child.get_connected_node()
                current_child = current_parent.get_addtion_child(current_child)
                current_parent_set.append(current_parent)
                current_child_set.append(current_child)

            for i in range(len(current_parent_set)):
                current_parent_set[i].add_child(current_child_set[i])

        return self.parent_set

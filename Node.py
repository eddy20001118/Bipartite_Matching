class Node:
    name = ""
    node_type = ""
    child = None
    parent = None
    avail_set = []
    parent_set = []
    child_set = []
    index = []
    has_connected = False
    initially_unconnected = False

    @classmethod
    def add_to_list(cls, node_type, this):
        if node_type is "parent":
            cls.parent_set.append(this)
        elif node_type is "child":
            cls.child_set.append(this)

    @classmethod
    def remove_from_list(cls, this):
        if this.node_type is "parent":
            cls.parent_set.remove(this)
        elif this.node_type is "child":
            cls.child_set.remove(this)

    @classmethod
    def remove_all(cls, type):
        if type is "parent":
            cls.parent_set = []
        elif type is "child":
            cls.child_set = []

    def __init__(self, node_type, name):
        self.name = name
        self.node_type = node_type
        self.add_to_list(node_type, self)

    def __repr__(self):
        return "{:s} : {:s}".format(self.node_type, self.name)

    def add_child(self, child):
        if child.parent is not None:
            old_parent = child.parent
            old_parent.child = None
        self.child = child
        self.child.parent = self
        self.has_connected = True
        self.child.has_connected = True

    def is_connected(self):
        is_connected = (self.parent is not None) or (self.child is not None)
        return is_connected

    def get_connected_node(self):
        if self.node_type == "parent":
            return self.child
        elif self.node_type == "child":
            return self.parent
        else:
            return None

    def get_addtion_child(self, current_node):
        for node in self.avail_set:
            if not node.is_connected():
                return node

        for node in self.avail_set:
            if node is not current_node and not node.parent.has_connected:
                return node

        for node in self.avail_set:
            if node is not current_node and not node.parent.initially_unconnected:
                return node

        for node in self.avail_set:
            if node is not current_node:
                return node

        return None

    def get_available_set(self):
        return self.avail_set

    def get_available_set_str(self):
        res = "{{ {:s} }}"
        temp = ""
        for i in range(len(self.avail_set)):
            child = self.avail_set[i]
            info = ""
            if i is 0:
                info = "{:s}".format(child.name)
            else:
                info = ", {:s}".format(child.name)
            temp += info
        return res.format(temp)

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_availablity(self, avail_set):
        self.avail_set = avail_set

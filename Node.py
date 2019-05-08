class Node:
    parent_set = []
    child_set = []

    name = ""
    node_type = ""
    connected_node = None
    avail_set = []
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
        if child.connected_node is not None:
            old_parent = child.connected_node
            old_parent.connected_node = None

        child.connected_node = self
        self.connected_node = child

        self.has_connected = True
        self.connected_node.has_connected = True

    def is_connected(self):
        return self.connected_node is not None

    def get_connected_node(self):
        return self.connected_node

    def get_addtion_child(self, current_node):
        for node in self.avail_set:
            if not node.is_connected():
                return node

        for node in self.avail_set:
            if node is not current_node and not node.connected_node.has_connected:
                return node

        for node in self.avail_set:
            if node is not current_node and not node.connected_node.initially_unconnected:
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

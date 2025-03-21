class Node:
    def __init__(self, node_id, labels=None, properties=None):
        self.node_id = node_id
        self.labels = [str(label) for label in labels] if labels else []  # Switch to list
        self.properties = properties if properties else {}
        print(f"Node created: id={self.node_id}, labels={self.labels}, properties={self.properties}")

    def add_label(self, label):
        self.labels.append(str(label))

    def set_property(self, key, value):
        self.properties[key] = value

    def __repr__(self):
        return f"Node(id={self.node_id}, labels={self.labels}, properties={self.properties})"
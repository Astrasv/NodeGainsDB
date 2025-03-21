from collections import defaultdict

class Index:
    def __init__(self):
        self.label_index = defaultdict(list)  # label -> list of node_ids
        self.property_index = {}  # label -> {prop: {value: list of node_ids}}
        self.rel_type_index = defaultdict(list)  # rel_type -> list of edge_ids
        print("Index initialized")

    def add_node(self, node):
        print(f"Adding node to index: {node}")
        if not isinstance(node.labels, (list, tuple)):
            raise ValueError(f"Bro, node.labels must be a list, got {type(node.labels)}: {node.labels}")
        for label in node.labels:
            if not isinstance(label, str):
                raise ValueError(f"Bro, labels must be strings, got {type(label)}: {label}")
            self.label_index[label].append(node.node_id)
            if label not in self.property_index:
                self.property_index[label] = {}
            prop_dict = self.property_index[label]
            print(f"Indexing label={label}, prop_dict={prop_dict}")
            for prop, value in node.properties.items():
                if prop not in prop_dict:
                    prop_dict[prop] = {}
                if value not in prop_dict[prop]:
                    prop_dict[prop][value] = []
                prop_dict[prop][value].append(node.node_id)

    def add_edge(self, edge):
        self.rel_type_index[edge.relationship_type].append(edge.edge_id)

    def get_nodes_by_label(self, label):
        return self.label_index.get(label, [])

    def get_nodes_by_property(self, label, prop, value):
        return self.property_index.get(label, {}).get(prop, {}).get(value, [])

    def get_edges_by_type(self, rel_type):
        return self.rel_type_index.get(rel_type, [])
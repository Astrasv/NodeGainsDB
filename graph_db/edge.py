class Edge:
    def __init__(self, edge_id, from_node, to_node, relationship_type, properties=None):
        self.edge_id = edge_id
        self.from_node = from_node
        self.to_node = to_node
        self.relationship_type = relationship_type
        self.properties = properties if properties else {}
        print(f"Edge created: id={self.edge_id}, from={self.from_node}, to={self.to_node}, type={self.relationship_type}")

    def set_property(self, key, value):
        self.properties[key] = value

    def __repr__(self):
        return f"Edge(id={self.edge_id}, from={self.from_node}, to={self.to_node}, type={self.relationship_type}, properties={self.properties})"
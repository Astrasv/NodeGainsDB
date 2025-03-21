from .node import Node
from .edge import Edge
from .index import Index
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.adjacency = defaultdict(list)
        self.node_counter = 0
        self.edge_counter = 0
        self.index = Index()
        print("Graph initialized")

    def create_node(self, labels=None, properties=None):
        node_id = self.node_counter
        self.node_counter += 1
        node = Node(node_id, labels, properties)
        self.nodes[node_id] = node
        self.index.add_node(node)
        return node

    def create_edge(self, from_node_id, to_node_id, relationship_type, properties=None):
        if from_node_id not in self.nodes or to_node_id not in self.nodes:
            raise ValueError("One or both nodes don’t exist, bro!")
        edge_id = self.edge_counter
        self.edge_counter += 1
        edge = Edge(edge_id, from_node_id, to_node_id, relationship_type, properties)
        self.edges[edge_id] = edge
        self.adjacency[from_node_id].append((edge_id, to_node_id))
        self.index.add_edge(edge)
        return edge

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def get_edge(self, edge_id):
        return self.edges.get(edge_id)
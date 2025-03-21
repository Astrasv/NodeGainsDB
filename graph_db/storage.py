import json
import os
from graph_db.node import Node
from graph_db.edge import Edge
from graph_db.index import Index

class Storage:
    def __init__(self, filepath="gains_data.json"):
        self.filepath = filepath

    def save(self, graph):
        data = {
            "nodes": {str(k): {"labels": list(v.labels), "properties": v.properties} for k, v in graph.nodes.items()},
            "edges": {str(k): {"from_node": v.from_node, "to_node": v.to_node, "relationship_type": v.relationship_type, "properties": v.properties} for k, v in graph.edges.items()},
            "node_counter": graph.node_counter,
            "edge_counter": graph.edge_counter
        }
        with open(self.filepath, 'w') as f:
            json.dump(data, f)
        print(f"Saved data to {self.filepath}")

    def load(self, graph):
        if not os.path.exists(self.filepath):
            print(f"No {self.filepath} found, starting fresh")
            return
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            graph.node_counter = data["node_counter"]
            graph.edge_counter = data["edge_counter"]
            graph.nodes.clear()
            graph.edges.clear()
            graph.adjacency.clear()
            graph.index = Index()
            print("Loading nodes...")
            for node_id, node_data in data["nodes"].items():
                labels = [str(label) for label in node_data["labels"]]  # Use list
                properties = node_data["properties"]
                node = Node(int(node_id), labels, properties)
                graph.nodes[int(node_id)] = node
                graph.index.add_node(node)
            print("Loading edges...")
            for edge_id, edge_data in data["edges"].items():
                edge = Edge(int(edge_id), edge_data["from_node"], edge_data["to_node"], edge_data["relationship_type"], edge_data["properties"])
                graph.edges[int(edge_id)] = edge
                graph.adjacency[edge_data["from_node"]].append((int(edge_id), edge_data["to_node"]))
                graph.index.add_edge(edge)
            print("Load complete")
from .graph import Graph

class GymQLParser:
    def __init__(self, graph):
        self.graph = graph

    def parse(self, query):
        query = query.strip().rstrip(";")
        query_upper = query.upper()
        print(f"Parsing query: {query}")
        if query_upper.startswith("LIFT"):
            return self._parse_lift(query)
        elif query_upper.startswith("SPOT"):
            return self._parse_spot(query)
        else:
            raise ValueError("Bro, use LIFT or SPOT for gains!")

    def _parse_lift(self, query):
        node_part = query.replace("LIFT", "").strip()
        print(f"LIFT node_part: {node_part}")
        if "-[" not in node_part:
            node_str = node_part.strip("()")
            label, props = self._parse_node(node_str)
            print(f"Parsed: label={label}, props={props}")
            node = self.graph.create_node([label], props)  # Pass as list
            return [node]
        else:
            start_node, rel, end_node = node_part.split(")-[")[0].strip(" ("), node_part.split(")-[")[1].split("]->(")[0], node_part.split("]->(")[1].strip(")")
            start_node = start_node.strip()
            end_node = end_node.strip()
            rel = rel.strip(":")
            start_label, start_props = self._parse_node(start_node)
            end_label, end_props = self._parse_node(end_node)
            n1 = self.graph.create_node([start_label], start_props)
            n2 = self.graph.create_node([end_label], end_props)
            edge = self.graph.create_edge(n1.node_id, n2.node_id, rel)
            return [n1, edge, n2]

    def _parse_spot(self, query):
        parts = query.split("GAINS")
        if len(parts) != 2:
            raise ValueError("No GAINS, bro? Fix your SPOT!")
        pattern = parts[0].replace("SPOT", "").strip()
        return_var = parts[1].strip()
        if ")-[" in pattern and "]->(" in pattern:
            start_node, rel, end_node = pattern.split(")-[")[0], pattern.split(")-[")[1].split("]->(")[0], pattern.split("]->(")[1]
            start_node = start_node.strip("()")
            end_node = end_node.strip("()")
            rel = rel.strip(":")
            start_label, start_props = self._parse_node(start_node)
            end_label, end_props = self._parse_node(end_node)
            start_nodes = self._find_nodes(start_label, start_props)
            results = []
            for node in start_nodes:
                for edge_id, target_id in self.graph.adjacency[node.node_id]:
                    edge = self.graph.get_edge(edge_id)
                    if edge.relationship_type == rel:
                        target_node = self.graph.get_node(target_id)
                        if (not end_label or end_label in target_node.labels) and self._match_props(target_node.properties, end_props):
                            results.append({return_var: target_node})
            return results
        else:
            node_str = pattern.strip("()")
            label, props = self._parse_node(node_str)
            nodes = self._find_nodes(label, props)
            return [{return_var: node} for node in nodes]

    def _parse_node(self, node_str):
        parts = node_str.split("{")
        label_part = parts[0].upper()
        label = label_part.split(":")[1] if ":" in label_part else None
        props = {}
        if len(parts) > 1:
            prop_str = parts[1].strip("}").replace("'", "").replace('"', '')
            for prop in prop_str.split(","):
                if ":" in prop:
                    key, value = prop.split(":")
                    props[key.strip()] = value.strip()
        return label, props

    def _find_nodes(self, label, props):
        if label:
            candidates = self.graph.index.get_nodes_by_label(label)
            nodes = [self.graph.get_node(nid) for nid in candidates]
            return [n for n in nodes if self._match_props(n.properties, props)]
        return []

    def _match_props(self, node_props, query_props):
        return all(k in node_props and node_props[k] == v for k, v in query_props.items())
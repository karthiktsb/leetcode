class GraphNode:
    def __init__(self, data, version):
        self.data = data
        self.version = version
        self.neighbors = []


def display_graph_nodes(node: GraphNode, seen):
    if node:
        if node not in seen:
            seen[node] = node
            print(str(node.data) + " - " + str(node.version))
            for p in node.neighbors:
                display_graph_nodes(p, seen)


def clone_graph(node: GraphNode, seen, version):
    if not node:
        return None

    root_new = GraphNode(node.data, version)
    seen[node] = node

    for p in node.neighbors:
        x = seen.get(p)
        if x:
            root_new.neighbors.append(x)
        else:
            root_new.neighbors.append(clone_graph(p, seen, version))

    return root_new


if __name__ == "__main__":
    root = GraphNode(0, 1)

    root.neighbors.append(GraphNode(1, 1))
    root.neighbors.append(GraphNode(2, 1))
    root.neighbors.append(GraphNode(3, 1))
    root.neighbors.append(GraphNode(4, 1))

    root.neighbors[0].neighbors.append(GraphNode(11, 1))
    root.neighbors[0].neighbors.append(GraphNode(12, 1))
    root.neighbors[0].neighbors.append(GraphNode(13, 1))

    root.neighbors[1].neighbors.append(GraphNode(21, 1))
    root.neighbors[1].neighbors.append(GraphNode(22, 1))

    root.neighbors[2].neighbors.append(GraphNode(31, 1))
    new_node = GraphNode(32, 1)
    new_node.neighbors.append(root)

    root.neighbors[2].neighbors.append(new_node)

    display_graph_nodes(root, {})

    new_root = clone_graph(root, {}, 2)

    display_graph_nodes(new_root, {})
    display_graph_nodes(root, {})

    root2 = GraphNode(80, 3)
    root3 = clone_graph(root2, {}, 5)

    display_graph_nodes(root3, {})


class LoadBalancer:

    def __init__(self, nodes):
        self.nodes = nodes
        self.current_node_index = 0

    def route_request(self, request):
        # round-robin strategy
        node = self.nodes[self.current_node_index]
        self.current_node_index = (self.current_node_index + 1) % len(self.nodes)
        return node

    def remove_node(self, node):
        # Check if the node exists in the list before removing it
        if node in self.nodes:
            self.nodes.remove(node)
        else:
            print("Node not found in the list of nodes.")

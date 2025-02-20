# Clone Graph: Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

class Node:
    def __init__(self, label):
        self.label = label
        self.neighbors = []

def cloneGraph(node):

    if node is None:
        return None

    old_to_new = {}

    def dfs(n):
        if n in old_to_new:
            return old_to_new[n]
        
        copy = Node(n.label)
        old_to_new[n] = copy

        for neighbor in n.neighbors:
            copy.neighbors.append(dfs(neighbor))
        
        return copy

    return dfs(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.neighbors = [node2, node3]
node2.neighbors = [node1, node3]
node3.neighbors = [node1, node2]

cloned = cloneGraph(node1)

def print_graph(node: Node, visited=None):
    if visited is None:
        visited = set()
    if node in visited:
        return
    visited.add(node)
    print(f"{node.label}: {[n.label for n in node.neighbors]}")
    for neighbor in node.neighbors:
        print_graph(neighbor, visited)

print_graph(cloned)
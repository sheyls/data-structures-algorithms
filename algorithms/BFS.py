from collections import deque

def bfs(start_node):
    visited = set()
    queue = deque([start_node])
    
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        # Aquí puedes procesar el nodo actual (por ejemplo, imprimir su etiqueta)
        print(current.label)
        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return visited


class Node:
     def __init__(self, label):
         self.label = label
         self.neighbors = []

# Y construyes un grafo:
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node3]
node3.neighbors = [node1, node2]

# Ejecutamos BFS a partir de node1
visited_nodes = bfs(node1)

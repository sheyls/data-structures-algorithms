from collections import deque

def topological_sort(graph):
    """
    graph: diccionario donde cada clave es un nodo y su valor es una lista de nodos adyacentes (hijos)
    Retorna una lista con el orden topológico de los nodos, o None si hay ciclos.
    """
    # Calcular el grado de entrada (in-degree) de cada nodo
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Inicializar una cola con los nodos que tienen in-degree 0
    queue = deque([node for node in graph if in_degree[node] == 0])
    top_order = []

    while queue:
        current = queue.popleft()
        top_order.append(current)
        # Disminuir el in-degree de los vecinos
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Si top_order contiene todos los nodos, es un orden topológico válido.
    if len(top_order) == len(graph):
        return top_order
    else:
        # Existe un ciclo, no se puede obtener un orden topológico
        return None

# Ejemplo de uso:
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

order = topological_sort(graph)
print("Orden topológico:", order)

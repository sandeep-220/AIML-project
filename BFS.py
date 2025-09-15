
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            queue.extend([neighbor for neighbor in graph.get(vertex, []) if neighbor not in visited])
    return order

if __name__ == "__main__":
    # Example usage
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("BFS traversal starting from 'A':", bfs(graph, 'A'))

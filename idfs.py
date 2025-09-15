
def dls(graph, node, goal, depth, visited=None):
	if visited is None:
		visited = set()
	if depth == 0 and node == goal:
		return [node]
	if depth > 0:
		visited.add(node)
		for neighbor in graph.get(node, []):
			if neighbor not in visited:
				path = dls(graph, neighbor, goal, depth-1, visited)
				if path:
					return [node] + path
	return None

def iddfs(graph, start, goal, max_depth):
	for depth in range(max_depth + 1):
		visited = set()
		path = dls(graph, start, goal, depth, visited)
		if path:
			return path
	return None

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
	path = iddfs(graph, 'A', 'F', 3)
	print("IDDFS path from 'A' to 'F':", path)
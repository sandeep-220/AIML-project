
import heapq

def a_star(graph, start, goal, h):
	open_set = []
	heapq.heappush(open_set, (h(start), start))
	came_from = {}
	g_score = {start: 0}

	while open_set:
		_, current = heapq.heappop(open_set)
		if current == goal:
			path = []
			while current in came_from:
				path.append(current)
				current = came_from[current]
			path.append(start)
			return path[::-1]
		for neighbor, cost in graph.get(current, []):
			tentative_g_score = g_score[current] + cost
			if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = tentative_g_score
				f_score = tentative_g_score + h(neighbor)
				heapq.heappush(open_set, (f_score, neighbor))
	return None

if __name__ == "__main__":
	# Example graph: each node maps to a list of (neighbor, cost)
	graph = {
		'A': [('B', 1), ('C', 3)],
		'B': [('D', 1), ('E', 5)],
		'C': [('F', 2)],
		'D': [],
		'E': [('F', 1)],
		'F': []
	}
	# Example heuristic: straight-line distance (dummy values)
	def heuristic(node):
		h_values = {'A': 6, 'B': 4, 'C': 5, 'D': 2, 'E': 2, 'F': 0}
		return h_values.get(node, 0)
	path = a_star(graph, 'A', 'F', heuristic)
	print("A* path from 'A' to 'F':", path)

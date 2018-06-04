from collections import defaultdict


class Graph:
	def __init__(self, count_vertices):
		self.count_vertices = count_vertices
		self.graph = defaultdict(list)

	def add_edge(self, n1, n2):
		self.graph[n1].append(n2)

	def topo_sort(self):
		visited = [False] * self.count_vertices
		stack = []

		for node in range(self.count_vertices):
			if not visited[node]:
				self.util_topo_sort(node, visited, stack)

		print stack

	def util_topo_sort(self, node, visited, stack):
		visited[node] = True
		for neighbor_node in self.graph[node]:
			if not visited[neighbor_node]:
				self.util_topo_sort(neighbor_node, visited, stack)

		stack.insert(0, node)

	def print_graph(self):
		for n1, n2 in self.graph.items():
			print n1, n2

graph = Graph(6)
graph.add_edge(5, 2)
graph.add_edge(5, 0)
graph.add_edge(4, 0)
graph.add_edge(4, 1)
graph.add_edge(2, 3)
graph.add_edge(3, 1)

graph.print_graph()

graph.topo_sort()
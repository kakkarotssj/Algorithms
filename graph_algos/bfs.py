# BFS FOR DIRECTED GRAPH

from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, n1, n2):
		self.graph[n1].append(n2)

	def print_graph(self):
		for n1, n2 in self.graph.items():
			print n1, n2

	def do_bfs(self, start):
		visited = [False] * len(self.graph)
		queue = [start]

		while queue:
			temp = queue.pop(0)
			visited[temp] = True
			print temp,

			for n2 in self.graph[temp]:
				if not visited[n2]:
					queue.append(n2)


graph = Graph()
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(0, 2)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(3, 3)

graph.print_graph()


print "Traversing graph using bfs"
print "Enter node you wish to start"
start = input()
graph.do_bfs(start)

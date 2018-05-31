# DFS FOR DIRECTED GRAPH

from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, n1, n2):
		self.graph[n1].append(n2)

	def print_graph(self):
		for n1, n2 in self.graph.items():
			print n1, n2

	def do_dfs(self, start):
		visited = [False] * len(self.graph)
		print visited

		self.dfs_util(start, visited)

	def dfs_util(self, node, visited):
		visited[node] = True
		print node, 

		for i in self.graph[node]:
			if not visited[i]:
				self.dfs_util(i, visited)

graph = Graph()
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(0, 2)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(3, 3)

graph.print_graph()


print "Traversing graph using dfs"
print "Enter node you wish to start"
n = input()
graph.do_dfs(n)

from collections import defaultdict
graph = defaultdict(list)

def addedge(node1, node2):
	graph[node1].append(node2)
	graph[node2].append(node1)

vertices_count = 5
addedge(0, 1)
addedge(0, 2)
addedge(1, 3)
addedge(1, 4)
addedge(3, 4)


def findparent(parent, node):
	if parent[node] == -1:
		return node
	else:
		return findparent(parent, parent[node])

def union(parent, n1set, n2set):
	parent[n1set] = n2set

def iscyclic(graph, vertices_count):
	parent = [-1] * vertices_count
	visited = [False] * vertices_count

	for n1 in range(vertices_count):
		for n2 in graph[n1]:
			if not visited[n2]:
				n1set = findparent(parent, n1)
				n2set = findparent(parent, n2)
				if n1set == n2set:
					return True
				else:
					union(parent, n1set, n2set)
				visited[n1] = True
	return False

if iscyclic(graph, vertices_count):
	print "Graph contains a cycle"
else:
	print "Graph does not contain a cycle"
def addedge(graph, node1, node2, weight):
	graph.append([node1, node2, weight])
	graph.append([node2, node1, weight])

def sortgraph(graph):
	graph.sort(key=lambda x:x[2])

def findparent(parent, node):
	if parent[node] == -1:
		return node
	else:
		return findparent(parent, parent[node])


def union(parent, n1set, n2set):
	parent[n1set] = n2set


def kruskalMST(graph, vertices_count):
	sortgraph(graph)
	parent = [-1] * vertices_count
	result = []

	edges = 0
	i = 0
	done = []
	while edges != vertices_count-1:
		minweighted_edge = graph[i]
		if set(minweighted_edge) in done:
			n1, n2, weight = minweighted_edge[0], minweighted_edge[1], minweighted_edge[2]
			n1set = findparent(parent, n1)
			n2set = findparent(parent, n2)
			if n1set == n2set:
				# dont include this edge
				pass
			else:
				union(parent, n1set, n2set)
				edges += 1
				result.append(minweighted_edge)
		else:
			pass
		i += 1
		done.append(set(minweighted_edge))

	return result


def printMST(mst):
	for edge in mst:
		print "%s --- %s" %(edge[0], edge[1])


def main():
	graph = []

	vertices_count = 9
	addedge(graph, 0, 1, 4)
	addedge(graph, 0, 7, 8)
	addedge(graph, 1, 7, 11)
	addedge(graph, 1, 2, 8)
	addedge(graph, 7, 8, 7)
	addedge(graph, 7, 6, 1)
	addedge(graph, 2, 8, 2)
	addedge(graph, 8, 6, 6)
	addedge(graph, 2, 3, 7)
	addedge(graph, 2, 5, 4)
	addedge(graph, 6, 5, 2)
	addedge(graph, 3, 5, 14)
	addedge(graph, 5, 4, 10)
	addedge(graph, 3, 4, 9)
	# addedge(graph, 0, 1, 10)
	# addedge(graph, 0, 2, 6)
	# addedge(graph, 0, 3, 5)
	# addedge(graph, 1, 3, 15)
	# addedge(graph, 2, 3, 4)

	mst = kruskalMST(graph, vertices_count)
	printMST(mst)


if __name__ == "__main__":
	main()
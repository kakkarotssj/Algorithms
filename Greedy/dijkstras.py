import heapq
import sys
import copy

def addedge(graph, node1, node2):
	graph[node1].append(node2)


def dijkstras(graph, count_vertices, startnode):
	vertices = [i for i in range(count_vertices)]
	
	d = [sys.maxsize+i for i in range(count_vertices-1)]
	d.insert(0, startnode)

	d_from_vertex = {}
	for i in range(count_vertices):
		d_from_vertex[i] = d[i]

	vertex_from_d = {}
	for i in range(count_vertices):
		vertex_from_d[d[i]] = i

	parent = [None for _ in range(count_vertices)]

	minheap = copy.deepcopy(d)
	heapq.heapify(minheap)

	while minheap:
		minvalue = heapq.heappop(minheap)
		vertex = vertex_from_d[minvalue]

		for adjacent_vertex in adjacent(graph, vertex):
			if d[adjacent_vertex] > d[vertex] + graph[vertex][adjacent_vertex]:
				d[adjacent_vertex] = d[vertex] + graph[vertex][adjacent_vertex]
				parent[adjacent_vertex] = vertex

	return parent, d


def adjacent(graph, vertex):
	adjacents = []
	for i in range(len(graph[vertex])):
		if i == vertex:
			continue
		else:
			if graph[vertex][i] == 0:
				pass
			else:
				adjacents.append(i)

	return adjacents

def main():
	count_vertices = 9
	# graph = [
	# 		[0, 10, 20, 0],
	# 		[10, 0 , 5, 16], 
	# 		[20, 5, 0, 20],
	# 		[0, 16, 20, 0]
	# 		]
	graph = [
		[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		]

	startnode = 0
   	result, distances = dijkstras(graph, count_vertices, startnode)

   	print distances

if __name__ == '__main__':
	main()

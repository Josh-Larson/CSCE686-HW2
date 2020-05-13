import graph as g


def iterative_calculate_mcm(edge_list):
	vertex_list = []
	final = []
	for edge in edge_list:
		if edge[0] not in vertex_list and edge[1] not in vertex_list:
			vertex_list.append(edge[0])
			vertex_list.append(edge[1])
			final.append(edge)
	return final


def calculate_mcm(graph):
	vertex_edge_count = {v: 0 for v in graph}
	edge_list = g.get_edge_list(graph)
	for e in edge_list:
		vertex_edge_count[e[0]] += 1
		vertex_edge_count[e[1]] += 1
	edge_list.sort(key=lambda e:  (vertex_edge_count[e[0]] + vertex_edge_count[e[1]]), reverse=False)
	return iterative_calculate_mcm(edge_list)

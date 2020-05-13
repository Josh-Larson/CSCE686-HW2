import random
from graphviz import Graph


def create_graph(vertex_count, edge_count):
	graph = {i: [] for i in range(vertex_count)}
	for i in range(edge_count):
		src = random.randint(0, vertex_count-1)
		dst = random.randint(0, vertex_count-1)
		while src == dst or (src in graph and dst in graph[src]) or (dst in graph and src in graph[dst]):
			src = random.randint(0, vertex_count - 1)
			dst = random.randint(0, vertex_count - 1)
		if src in graph:
			graph[src].append(dst)
		else:
			graph[src] = [dst]
	return graph


def is_same_edge(edge1, edge2):
	return (edge1[0] == edge2[0] and edge1[1] == edge2[1]) or (edge1[0] == edge2[1] and edge1[1] == edge2[0])


def is_edge_in_list(edge, edge_list):
	for e in edge_list:
		if is_same_edge(edge, e):
			return True
	return False


def get_edge_list(graph):
	edges = []
	for src in graph:
		for dst in graph[src]:
			edges.append((src, dst))
	return edges


def render_graph(graph, edge_list, filename="graph", fmt="pdf"):
	g = Graph(format=fmt)
	for src in graph:
		g.node(name=str(src))
	for src in graph:
		for dst in graph[src]:
			g.edge(str(src), str(dst), color="red" if is_edge_in_list((src, dst), edge_list) else "black")
	g.render(filename=filename)

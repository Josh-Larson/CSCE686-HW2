import graph as g
import networkx as nx

def calculate_mcm(graph):
	G = nx.Graph()
	for v in graph:
		G.add_node(str(v))
	for v in graph:
		for e in graph[v]:
			G.add_edge(str(v), str(e))
	
	return [(int(left), int(right)) for left, right in nx.maximal_matching(G)]

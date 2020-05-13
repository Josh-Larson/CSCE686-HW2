import graph as g
import custom_mcm as cmcm
import random_mcm as rmcm
import networkx_mcm as nmcm
import time
import numpy as np
import matplotlib.pyplot as plt


def evaluate_heuristic(vertices, edges, render=False, print_stdout=False):
	graph = g.create_graph(vertices, edges)
	start = time.time()
	custom_mcm = cmcm.calculate_mcm(graph)
	end = time.time()
	custom_time = end - start
	if print_stdout:
		print("Custom Time:   %.3fms" % ((end - start) * 1000))
	start = time.time()
	random_mcm = rmcm.calculate_mcm(graph)
	end = time.time()
	if print_stdout:
		print("Random Time:   %.3fms" % ((end - start) * 1000))
	start = time.time()
	brute_force_mcm = nmcm.calculate_mcm(graph)
	end = time.time()
	networkx_time = end - start
	if print_stdout:
		print("NetworkX Time: %.3fms" % ((end - start) * 1000))
		print(custom_mcm)
		print(random_mcm)
		print(brute_force_mcm)
	if render:
		g.render_graph(graph, custom_mcm, filename='networkx', fmt="png")
		g.render_graph(graph, random_mcm, filename='random', fmt="png")
		g.render_graph(graph, brute_force_mcm, filename='heuristic', fmt="png")
	return 1 - len(custom_mcm) / len(brute_force_mcm), 1 - len(random_mcm) / len(brute_force_mcm), custom_time, networkx_time


def main_evalutate():
	performance = np.zeros((60, 2))
	timing = np.zeros((60, 2))
	for vertices in range(2, 62):
		avg_custom = 0
		avg_random = 0
		avg_time_custom = 0
		avg_time_networkx = 0
		for i in range(20):
			eval = evaluate_heuristic(vertices*10, vertices*10-1)
			avg_custom += eval[0]
			avg_random += eval[1]
			avg_time_custom += eval[2]
			avg_time_networkx += eval[3]
		avg_custom /= 20
		avg_random /= 20
		avg_time_custom /= 20
		avg_time_networkx /= 20
		performance[vertices-2, 0] = -avg_custom * 100
		performance[vertices-2, 1] = -avg_random * 100
		timing[vertices-2, 0] = avg_time_custom
		timing[vertices-2, 1] = avg_time_networkx
	edge_count = np.arange(60)*10 + 1
	plt.plot(edge_count, performance[:, 0], 'r-', label="Heuristic")
	plt.plot(edge_count, performance[:, 1], 'g-', label="Random")
	plt.suptitle("Comparison of Maximal Cardinality Matching Algorithms")
	plt.legend(loc="upper left")
	plt.xlabel("Edge Count")
	plt.ylabel("Percent Increase in Maximum Cardinality Matches")
	plt.savefig("Visualizations/EdgeCountComparison.png", dpi=360)
	plt.savefig("Visualizations/EdgeCountComparison.pdf")
	plt.show()
	
	plt.clf()
	plt.plot(edge_count, timing[:, 0] * 1000, 'r-', label="Heuristic")
	plt.plot(edge_count, timing[:, 1] * 1000, 'g-', label="NetworkX")
	plt.suptitle("Comparison of Runtime Between Algorithms")
	plt.legend(loc="upper left")
	plt.xlabel("Edge Count")
	plt.ylabel("Time to Compute (ms)")
	plt.savefig("Visualizations/TimingComparison.png", dpi=360)
	plt.savefig("Visualizations/TimingComparison.pdf")
	plt.show()


def main_graphs():
	graph = g.create_graph(16, 30)
	g.render_graph(graph, cmcm.calculate_mcm(graph), "Visualizations/heuristic")
	g.render_graph(graph, nmcm.calculate_mcm(graph), "Visualizations/networkx")
	

# main_evalutate()
main_graphs()

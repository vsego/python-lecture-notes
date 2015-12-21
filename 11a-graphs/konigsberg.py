#!/usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image
from os import system

#G = nx.complete_graph(5)
G = nx.MultiGraph()

#G.add_nodes_from(["C", "A", "D", "B"])
#G.add_edges_from([{"C","A"}, {"C","A"}, {"A","B"}, {"A","B"}, {"C", "D"}, {"A", "D"}, {"B", "D"}])
G.add_edges_from([("C","A"), ("C","A"), ("A","B"), ("A","B"), ("C", "D"), ("A", "D"), ("B", "D")])
#G.add_edges_from([("C","A"), ("A","B"), ("C", "D"), ("A", "D"), ("B", "D")])
#G.add_edges_from([("C","A"), ("C","A"), ("A","B"), ("A","B"), ("C", "D"), ("A", "D"), ("B", "D"), ("A", "C"), ("B", "D")])
print("Nodes:", G.nodes())
print("Edges:", G.edges())
print("Nodes:", ", ".join(sorted(G.nodes())))
print("Edges:", ", ".join(sorted("{{{}}}".format(",".join(sorted(t))) for t in G.edges())))
print("The graph {} Eulerian.".format("is" if nx.is_eulerian(G) else "is not"))

spt = nx.minimum_spanning_edges(G, data=False)
print(list(spt))
#print("Edges:", ", ".join(sorted("{{{}}}".format(",".join(sorted(t))) for t in spt)))
#nx.set_node_attributes(G, "pos", {"C": { "pos": (0,2) }, "A": { "pos": (0,1) }, "D": { "pos": (1,0) }, "B": (0,0)})
#nx.draw_networkx(G, pos={"C": (0,2), "A": (0,1), "D": (1,0), "B": (0,0)})
#plt.axis("off")
#plt.show()

#nx.write_dot(G, "konigsberg.dot")
#system("circo -T png konigsberg.dot > konigsberg.png")
#img = Image.open('konigsberg.png')
#img.show()

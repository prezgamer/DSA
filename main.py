import json
import os
import networkx as nx
import matplotlib.pyplot as plt

from ParseToMatrix import ParseToMatrix
from TrimRoutes import TrimRoutes

def main():
    adjMatrix = ParseToMatrix()
    N = len(adjMatrix)
    
    G = nx.DiGraph()
    
    for i in range(N):
        for j in range(N):
            if adjMatrix[i][j] == 1:
                G.add_edge(i,j)
                
    nx.draw(G, with_labels=True, node_color="lightblue", node_size=200, font_weight="bold")
    
    # WARNING: very laggy, takes a while to start the interactive display
    # plt.show()


if __name__ == "__main__":
    main()
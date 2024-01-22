import networkx as nx 
import matplotlib.pyplot as plt

def graph_creating():
    G = nx.Graph()

    G.add_node("Riga")
    G.add_nodes_from(["Liepaja", "Kolka", "Dobele", "Ogre", "Jurmala", "Jelgava", "Ventspils"])
    G.add_edge("Riga", "Liepaja", weight = 8.65)
    G.add_edge("Riga", "Kolka", weight = 6.35)
    G.add_edge("Riga", "Dobele", weight = 3.35)
    G.add_edge("Riga", "Ogre", weight = 2.10)
    G.add_edge("Riga", "Jurmala", weight = 1.75)
    G.add_edge("Riga", "Jelgava", weight = 2.40)
    G.add_edge("Riga", "Ventspils", weight = 7.65)
    G.add_edge("Riga", "Saldus", weight = 5.15)

    G.add_edge("Liepaja", "Saldus", weight = 4.30)
    G.add_edge("Liepaja", "Ventspils", weight = 5.30)

    G.add_edge("Kolka", "Jurmala", weight = 5.45)

    G.add_edge("Dobele", "Jelgava", weight = 1.80)
    G.add_edge("Dobele", "Saldus", weight = 2.60)

    G.add_edge("Jurmala", "Ventspils", weight = 7.00)

    G.add_edge("Jelgava", "Ventspils", weight = 8.00)
    G.add_edge("Jelgava", "Saldus", weight = 3.80)

    G.add_edge("Ventspils", "Saldus", weight = 5.50)
    return G

    
    
if __name__ == "__main__":
    G = graph_creating()
    pos = nx.spring_layout(G, seed=42)
    pos["Ventspils"] = [-0.45, -0.75]
    pos["Kolka"] = [-0.45, 0.75]
    pos["Dobele"] = [0.45, 0.75]
    pos["Liepaja"] = [0.0, -0.3]
    pos["Jelgava"] = [0.45, -0.65]
    pos["Saldus"] = [0.2, -0.50]
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    print(G)
    print(G.degree)
    print(nx.degree_centrality(G))
    print(nx.betweenness_centrality(G))
    print(nx.closeness_centrality(G))

    plt.show()



import flet as ft

from model.modello import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()


ft.app(target=main)


# DFS (Depth First Search)
#
# nx.dfs_edges(G, source=nodo) → restituisce gli archi della visita
# nx.dfs_tree(G, source=nodo) → restituisce il grafo albero DFS
# list(nx.dfs_preorder_nodes(G, source=nodo)) → lista nodi in ordine di visita
#
# BFS (Breadth First Search)
#
# nx.bfs_edges(G, source=nodo) → restituisce gli archi della visita
# nx.bfs_tree(G, source=nodo) → restituisce il grafo albero BFS
# list(nx.bfs_layers(G, [nodo])) → nodi divisi per livello
#
# Cammini minimi
#
# nx.shortest_path(G, source=a, target=b, weight='weight') → cammino minimo
# nx.shortest_path_length(G, source=a, target=b, weight='weight') → solo la distanza
# nx.dijkstra_path(G, source=a, target=b, weight='weight') → equivalente con Dijkstra


# Non diretto → nx.connected_components(G)
# Diretto weakly → nx.weakly_connected_components(G)
# Diretto strongly → nx.strongly_connected_components(G)

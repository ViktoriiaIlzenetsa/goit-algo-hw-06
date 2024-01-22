from collections import deque

from task1 import graph_creating
from dfs import dfs_recursive
from bfs import bfs_recursive


if __name__ == "__main__":
    G = graph_creating()
    print(f"DFS with start in Riga")
    dfs_recursive(G, "Riga")
    print()
    print(f"BFS with start in Riga")
    bfs_recursive(G, deque(["Riga"]))
    print()
    print(f"DFS with start in Dobele")
    dfs_recursive(G, "Dobele")
    print()
    print(f"BFS with start in Dobele")
    bfs_recursive(G, deque(["Dobele"]))
   
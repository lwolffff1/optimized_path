from typing import Dict, List, Tuple, Iterable, Optional
import math

class Graph:
    def __init__(self, adjacency: Dict[str, List[Tuple[str, float]]]):
        
        self.edges: Dict[str, List[Tuple[str, float]]] = {}
        for u, nbrs in adjacency.items():
            self.edges[u] = list(nbrs)  
        
        for u, nbrs in list(self.edges.items()):
            for v, _ in nbrs:
                if v not in self.edges:
                    self.edges[v] = []

    def __repr__(self):
        graph_str = ""
        for node, neighbors in self.edges.items():
            graph_str += f"{node} -> {', '.join([f'{n}({w})' for n, w in neighbors])}\n"
        return graph_str

    # ==== main API ====
    def get_neighbors(self, node: str) -> List[Tuple[str, float]]:
        return self.edges.get(node, [])

    def neighbors(self, node: str) -> List[Tuple[str, float]]:
        
        return self.get_neighbors(node)

    
    def add_node(self, node: str):
        if node not in self.edges:
            self.edges[node] = []
        else:
            raise ValueError(f"Node {node} already exists.")

    def add_edge(self, u: str, v: str, w: float):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, w))  

    def remove_node(self, node: str):
        if node not in self.edges:
            raise ValueError(f"Node {node} does not exist.")
        del self.edges[node]
        for u in self.edges:
            self.edges[u] = [(v, w) for (v, w) in self.edges[u] if v != node]

    def remove_edge(self, u: str, v: str):
        if u not in self.edges:
            raise ValueError(f"Node {u} does not exist.")
        before = len(self.edges[u])
        self.edges[u] = [(x,w) for (x,w) in self.edges[u] if x != v]
        if len(self.edges[u]) == before:
            raise ValueError(f"Edge {u}->{v} does not exist.")
    
    ## dijkstra
    def shortest_distances(self, source: str) -> Dict[str, float]:
        if source not in self.edges:
            raise ValueError(f"Source node {source} does not exist.")
        distances = {node: math.inf for node in self.edges}
        distances[source] = 0
        visited = set()
        while len(visited) < len(self.edges):
            current_node = min((node for node in self.edges if node not in visited), key=lambda node: distances[node])
            visited.add(current_node)
            for neighbor, weight in self.edges[current_node]:
                if neighbor not in visited:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
        return distances
    
class Grid:
    def __init__(self, lines: List[str]):
        
        if not lines or not all(isinstance(r, str) for r in lines):
            raise ValueError("lines must be a non-empty list of strings")
        
        w = len(lines[0])

        if w ==0:
            raise ValueError("lines must not be empty")
        if any(len(r) != w for r in lines):
            raise ValueError("all rows must have the same length")
        self.grid = lines
        self.h = len(lines)
        self.w = w

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.h and 0 <= c < self.w

    def passable(self, r: int, c: int) -> bool:
        return self.grid[r][c] != '#'

    def neighbors(self, r: int, c: int) -> Iterable[Tuple[int, int]]:
        for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
            nr, nc = r + dr, c + dc
            if self.in_bounds(nr, nc) and self.passable(nr, nc):
                yield (nr, nc)

    @staticmethod
    def dist(a: Tuple[int,int], b: Tuple[int,int]) -> float:
        
        return 1.0
        


# Shortest Path Algorithms (Dijkstra & A*)

This is a Python project that demonstrates shortest path finding using **Dijkstra's algorithm** (for general weighted graphs) and **A\*** (for grid maps with heuristics).  
It includes a command-line interface (CLI), unit tests, and example datasets.

## Project Structure

shortest-path/
├─ shortest_path/
│ ├─ graph.py # Graph & Grid implementations
│ ├─ heuristics.py # heuristic functions (zero, manhattan, euclidean)
│ ├─ algorithms/
│ │ ├─ dijkstra.py # Dijkstra algorithm
│ │ └─ astar.py # A* algorithm
│ └─ io_utils.py # utilities for reading input
├─ examples/
│ ├─ tiny_edges.csv # graph example
│ └─ tiny_grid.txt # grid example
├─ tests/ # pytest unit tests
│ ├─ test_dijkstra.py
│ └─ test_astar.py
├─ cli.py # command-line interface
└─ README.md

Usage: 
1. Run Dijkstra on a general graph: python cli.py graph --file examples/tiny_edges.csv --src A --dst D
2. Run A* on a grid with Manhattan heuristic: python cli.py grid --file examples/tiny_grid.txt --start 0,0 --goal 5,6 --heuristic manhattan


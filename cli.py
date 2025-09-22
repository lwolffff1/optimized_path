import argparse
from shortest_path.graph import Graph, Grid
from shortest_path.io_utils import read_edge_list_csv, read_grid_txt
from shortest_path.algorithms.dijkstra import dijkstra
from shortest_path.algorithms.astar import astar_grid
from shortest_path import heuristics

def main():
    ap = argparse.ArgumentParser(description="Shortest path demo (Dijkstra & A*)")
    sub = ap.add_subparsers(dest="mode", required=True)

    g1 = sub.add_parser("graph", help="run on general graph (edge list csv)")
    g1.add_argument("--file", required=True)
    g1.add_argument("--src", required=True)
    g1.add_argument("--dst", required=True)
    g1.add_argument("--algo", choices=["dijkstra"], default="dijkstra")

    g2 = sub.add_parser("grid", help="run on grid map (txt)")
    g2.add_argument("--file", required=True)
    g2.add_argument("--start", required=True, help="r,c (0-based)")
    g2.add_argument("--goal", required=True, help="r,c (0-based)")
    g2.add_argument("--algo", choices=["astar"], default="astar")
    g2.add_argument("--heuristic", choices=["zero","manhattan","euclidean"], default="manhattan")

    args = ap.parse_args()

    if args.mode == "graph":
        adj = read_edge_list_csv(args.file)
        g = Graph(adj)
        if args.algo == "dijkstra":
            dist, path = dijkstra(g, args.src, args.dst)
        print(f"dist={dist}")
        print("path=", " -> ".join(path) if path else "(no path)")

    else: # grid
        lines = read_grid_txt(args.file)
        grid = Grid(lines)
        start = tuple(map(int, args.start.split(",")))
        goal = tuple(map(int, args.goal.split(",")))
        h = getattr(heuristics, args.heuristic)
        dist, path = astar_grid(grid, start, goal, h)
        print(f"dist={dist}")
        print("path=", path if path else "(no path)")

if __name__ == "__main__":
    main()
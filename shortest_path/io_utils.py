import csv

def read_edge_list_csv(path: str):
    # format: u,v,weight (header optional)
    adj = {}
    with open(path, newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        # bỏ header nếu có chữ
        if rows and not rows[0][2].replace('.','',1).isdigit():
            rows = rows[1:]
        for u, v, w in rows:
            w = float(w)
            adj.setdefault(u, []).append((v, w))
            adj.setdefault(v, [])  # ensure existence if no outgoing
    return adj

def read_grid_txt(path: str):
    with open(path) as f:
        lines = [line.rstrip('\n') for line in f]
    return lines
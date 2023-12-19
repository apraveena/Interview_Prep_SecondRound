#pseudocode
import math

def neg_wt_edges(n, edges, source, dest):
    table = [math.inf] * n
    table[source] = 0
    for i in range(n-1):
        for u, v, w in edges:
            table[v] = min(table[v], table[u] + w)
    return table[dest]

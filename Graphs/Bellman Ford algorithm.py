#Pseudocode
#best path from source to destination in k hops
def bellman_ford_algorithm(n, edges, src, dest, k):
    table = [[] for _ in range(n)] # range(2)?
    for hops in range(1, k + 1):
        # fill in the entries in column = hops
        for v in range(0, n-1):
            #only keeping 2 columns
            table[v][hops % 2] = table[v][(hops - 1) % 2]
            for u, v, w in edges:
                table[v][hops % 2] = min (table[v][hops % 2], table[v][(hops - 1) % 2] + w)
    return table[dest][(k + 1) % 2]
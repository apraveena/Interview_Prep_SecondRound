
def quick_find(n, edges):
    component_ids = [x for x in range(n)]
    no_of_components = n
    print(component_ids)
    for u, v in edges:
        # find part - O(1)
        if component_ids[u] != component_ids[v]:
            old_id = component_ids[u]
            # union does the most work - O(n^2)
            for node in range(len(component_ids)):
                if component_ids[node] == old_id:
                    component_ids[node] = v
            print(f"{u}--{v}")
            print(component_ids)
            no_of_components -= 1
        print(no_of_components)

def quick_union(n, edges):
    parent = [x for x in range(n)]
    no_of_components = n
    def find_root(x):
        while x != parent[x]:
            x = parent[x]
        return x

    for u, v in edges:
        lu = find_root(u)
        lv = find_root(v)
        if lu != lv:
            parent[lu] = lv
            no_of_components -= 1
        print(no_of_components)

#Weighted quick union - added size array to keep track of number of nodes
def union_find(n, edges):
    parent = [x for x in range(n)]
    size = [1 for _ in range(n)]
    no_of_components = n
    def find_root(x):
        while x != parent[x]:
            x = parent[x]
        return x

    for u, v in edges:
        lu = find_root(u)
        lv = find_root(v)
        if lu != lv:
            if size[lu] < size[lv]:
                parent[lu] = lv
                size[lv] += size[lu]
            else:
                parent[lv] = lu
                size[lu] += size[lv]
            no_of_components -= 1
        print(no_of_components)

#weighted quick union(because using size) + path compression
def union_find_with_path_compression(n, edges):
    parent = [i for i in range(n)]
    size = [1] * n
    def find_root(x):
        if parent[x] == x:
            return x
        root_x = find_root(x)
        parent[x] = root_x
        return root_x

    no_of_components = n

    for u, v in edges:
        lu = find_root(u)
        lv = find_root(v)
        if lu != lv:
            no_of_components -= 1
            if size[lu] < size[lv]:
                parent[lu] = lv
                size[lv] += size[lu]
            else:
                parent[lv] = lu
                size[lu] = size[lv]

    return no_of_components


# quick_find(n = 5, edges = [[0, 2], [2, 4], [4, 3], [3, 1], [1, 0]])
# quick_union(n = 5, edges = [[0, 2], [2, 4], [4, 3], [3, 1], [1, 0]])
union_find(n = 5, edges = [[0, 2], [2, 4], [4, 3], [3, 1], [1, 0]])




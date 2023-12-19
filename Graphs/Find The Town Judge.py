# def find_town_judge(n, trust):
#     """
#     Args:
#      n(int32)
#      trust(list_list_int32)
#     Returns:
#      int32
#     """
#     trust_map = {}
#     # sample trust_map
#     # { 4: [1, 2, 3],
#     #   1: [4]
#     # }
#     for from_, to_ in trust:
#         if to_ not in trust_map:
#             trust_map[to_] = [from_]
#         else:
#             trust_map[to_].append(from_)
#
#     judge_kv = sorted(trust_map.items(), key=lambda item: (-len(item[1])))[:1]
#     judge_kv = judge_kv[0]
#     # if rest of the pople trust judge
#     if len(judge_kv[1]) == n - 1:
#         for item in trust_map.values():
#             if item == judge_kv[0]:
#                 return -1
#         return judge_kv[0]
#
#     return -1


def find_town_judge(n, trust):
    """
    Args:
     n(int32)
     trust(list_list_int32)
    Returns:
     int32
    """
    # Whether I trust someone or some trusts me, I keep a count
    # If my count is more than n-1, then I must have trusted someone
    #  or if my count is less than n-1, someone must have not trusted me
    #  in both cases, I am not the trusted judge

    out_degree = [0] * (n + 1)
    in_degree = [0] * (n + 1)

    for from_, to_ in trust:
        out_degree[from_] += 1
        in_degree[to_] += 1

    for i in range(n + 1):
        if out_degree[i] == 0 and in_degree[i] == n - 1:
            return i
    return -1

print(find_town_judge(3, [[1, 2], [2, 3], [3, 1], [3, 2]]) == -1)
print(find_town_judge(4,  [[1, 4],[2, 4],[3, 4]]) == 4)
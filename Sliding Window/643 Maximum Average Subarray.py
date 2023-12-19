def max_avg_subarray(inp_list, k):
    global_sum = curr_sum = sum(inp_list[:k])
    if len(inp_list) < k: return global_sum
    for i in range(k, len(inp_list)):
        curr_sum += inp_list[i] - inp_list[i - k]
        global_sum = max(global_sum, curr_sum)

    return global_sum/k
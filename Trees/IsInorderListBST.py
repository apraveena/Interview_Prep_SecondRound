from typing import List

def is_bst(in_order_list: List[int]) -> bool:
    for i in range(len(in_order_list)-1):
        if in_order_list[i] > in_order_list[i + 1]:
            return False
    return True

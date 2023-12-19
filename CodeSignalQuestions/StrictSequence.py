def first_mismatch(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return i
    return -1


def is_strict_sequence_after_one_removal(sequence):
    if len(sequence) in (0, 1): return True
    mis_match = first_mismatch(sequence)
    if mis_match == -1:
        return True
    # removing first value makes it right?
    if first_mismatch(sequence[:mis_match] + sequence[mis_match + 1:]) == -1:
        return True
    # or removing second value makes it right?
    if first_mismatch(sequence[:mis_match + 1] + sequence[mis_match + 2:]) == -1:
        return True

    return False

print(is_strict_sequence_after_one_removal([3, 5, 67, 98, 3]) == True)

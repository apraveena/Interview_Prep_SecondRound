# Clarification questions
# 1. Are numbers positive?
# 2. is 0 considered even or odd
# 3. Size of data - 1 <= size <= 100000
# 4. Range of data
# 5. Can I used auxiliary space - No
# 6. Stable algorithm? - No
# Linear complexity - O(1) auxiliary space

def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    even = 0
    odd = len(numbers) - 1
    start = 0
    while odd >= even:
        if numbers[even] % 2 == 0:
            even += 1
        elif numbers[odd] % 2 != 0:
            odd -= 1
        else:
            numbers[even], numbers[odd] = numbers[odd], numbers[even]
            even += 1
            odd -= 1

    return numbers
# A dieter consumes calories[i] calories on the i-th day.
#
# Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):
#
# If T < lower, they performed poorly on their diet and lose 1 point;
# If T > upper, they performed well on their diet and gain 1 point;
# Otherwise, they performed normally and there is no change in points.
# Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for calories.length days.
#
# Note that the total points can be negative.
def diet_plan(inp_list, k, lower, upper):
    final_sum = 0
    curr_sum = sum(inp_list[:k])
    if curr_sum < lower:
        final_sum -= 1
    elif curr_sum > upper:
        final_sum += 1

    for i in range(k, len(inp_list)):
        curr_sum += inp_list[i] - inp_list[i - k]
        if curr_sum < lower:
            final_sum -= 1
        elif curr_sum > upper:
            final_sum += 1

    return final_sum

print(diet_plan([3,2], 2, 0, 1) == 1)
print(diet_plan([1, 2, 3, 4, 5], 1, 3, 3) == 0)

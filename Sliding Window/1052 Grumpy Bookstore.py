# There is a bookstore owner that has a store open for n minutes.Every minute, some number of customers enter the store.You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy.You are given a binary array grumpy where grumpy[i] is 1 if the
# bookstore owner is grumpy during the ith minute, and is 0 otherwise.
#
# When
# the
# bookstore
# owner is grumpy, the
# customers
# of
# that
# minute
# are
# not satisfied, otherwise, they
# are
# satisfied.
#
# The
# bookstore
# owner
# knows
# a
# secret
# technique
# to
# keep
# themselves
# not grumpy
# for minutes consecutive minutes, but can only use it once.
#
# Return
# the
# maximum
# number
# of
# customers
# that
# can
# be
# satisfied
# throughout
# the
# day.
#
# Example
# 1:
#
# Input: customers = [1, 0, 1, 2, 1, 1, 7, 5], grumpy = [0, 1, 0, 1, 0, 1, 0, 1], minutes = 3
# Output: 16
# Explanation: The
# bookstore
# owner
# keeps
# themselves
# not grumpy
# for the last 3 minutes.
# The
# maximum
# number
# of
# customers
# that
# can
# be
# satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
# Example
# 2:
#
# Input: customers = [1], grumpy = [0], minutes = 1
# Output: 1
# k = minutes
def grumpy_shopkeeper(customers, grumpy, k):
    happy_cust_count = 0

    for i in range(len(customers)):
        if grumpy[i] == 0:
            happy_cust_count += customers[i]

    final_happy_customers = 0
    curr_happy_customers = 0

    #Set the window
    for i in range(k):
        if grumpy[i] == 1: # assume I converted to happy customers
            curr_happy_customers += customers[i]

    for i in range(k, len(customers)):
        if grumpy[i] == 1:
            curr_happy_customers += customers[i]

        if grumpy[i - k] == 1:
            curr_happy_customers -= customers[i - k]

        final_happy_customers = max(final_happy_customers, curr_happy_customers)

    return final_happy_customers + happy_cust_count

print(grumpy_shopkeeper([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) == 16)




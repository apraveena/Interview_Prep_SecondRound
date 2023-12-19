# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
# Example 1:
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

def perm_in_string(s1, s2):
    '''

    :param s1: subset string that we are looking to find in s2
    :param s2:
    :return:
    '''
    hmap1, hmap2 = {}, {}
    k = len(s1) # this is the fixed length we are looking to match
    for i in range(k):
        hmap1[s1[i]] = hmap1.get(s1[i], 0) + 1

    for i in range(k):
        hmap2[s2[i]] = hmap2.get(s2[i], 0) + 1

    if hmap1 == hmap2: return True

    for i in range(k, len(s2)):
        idx_to_remove = i - k
        if hmap2[s2[idx_to_remove]] == 1:
            hmap2.pop(s2[idx_to_remove])
        else:
            hmap2[s2[i]] -= 1

        hmap2[s2[i]] = hmap2.get(s2[i], 0) + 1
        if hmap1 == hmap2: return True

    return False

print(perm_in_string("ab", "eidbaooo") == True)
print(perm_in_string("ab", "eidboaoo") == False)
print(perm_in_string("acb", "eidbacoaoo") == True)

#Interview question in Kaya

# You are given a string s. Reorder the string using the following algorithm:
#
# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
#
# Return the result string after sorting s with this algorithm.

def sort_string(s):
    s = list(s)
    res = ""
    while s:
        for ltr in sorted(set(s)):
            res += ltr
            s.remove(ltr)
        for ltr in sorted(set(s), reverse=True):
            res += ltr
            s.remove(ltr)

    return res

print(sort_string("aabbcc"))
print(sort_string("aaaaaaaaaaabbbbbbbbbbcccccccc"))


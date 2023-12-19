def anagrams(s, p):
    res = []
    hmap_s, hmap_p = {}, {}
    k = len(p)
    for i in range(k):
        hmap_p[p[i]] = hmap_p.get(p[i], 0) + 1

    for i in range(k):
        hmap_s[s[i]] = hmap_s.get(s[i], 0) + 1

    if hmap_p == hmap_s:
        res.append(0)

    for i in range(k, len(s)):
        idx_to_remove = i - k
        #remove the first letter from hmap_s

        if hmap_s[s[idx_to_remove]] == 1:
            hmap_s.pop(s[idx_to_remove])
        else:
            hmap_s[s[idx_to_remove]] -= 1

        hmap_s[s[i]] = hmap_s.get(s[i], 0) + 1

        if hmap_s == hmap_p:
            res.append(i - k + 1)

    return res

print(anagrams("cbaebabacd", "abc") == [0, 6])
print(anagrams("abab", "ab") == [0, 1, 2])






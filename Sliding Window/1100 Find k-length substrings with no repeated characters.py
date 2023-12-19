def no_repeats(inp_str, k):
    hm = {}
    no_repeat_count = 0
    #set the window
    for i in range(k):
        if inp_str[i] in hm:
            hm[inp_str] += 1
        else:
            hm[inp_str[i]] = 1
    if len(hm) == k:
        no_repeat_count += 1

    for i in range(k, len(inp_str)):
        if hm[inp_str[i - k]] == 1:
            del hm[inp_str[i - k]]
        else:
            hm[inp_str[i - k]] -= 1
        if inp_str[i] in hm:
            hm[inp_str[i]] += 1
        else:
            hm[inp_str[i]] = 1
            if len(hm) == k: no_repeat_count += 1

    return no_repeat_count

print(no_repeats("manners", 2) == 5)
print(no_repeats("havefunonleetcode", 5) == 6) #"havef", "avefu", "vefun", "efuno", "etcod", "tcode" #havefunonleetcode
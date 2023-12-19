def sub_str(s, c, start, end):
    count = 0
    for i in range(start, end+1):
        count += 1 if s[i] == c else 0

    return count

s = "captialone"
c = "a"
print(sub_str(s, c, 0, 4))
s = "captialone"
c = "a"
print(sub_str(s, c, 0, 9))

def sub_str_scale_out_preprocess(s, c, start, end):
    freq
    for i in range(start, end+1):
        count += 1 if s[i] == c else 0

    return count
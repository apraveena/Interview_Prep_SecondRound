def max_no_of_vowels(inp_str, k):
    curr_no_of_vowels = 0

    #setting the window
    for i in range(k):
        if inp_str[i] in "aeiou":
            curr_no_of_vowels += 1

    global_no_of_vowels = curr_no_of_vowels

    for i in range(k, len(inp_str)):
        if inp_str[i] in "aeiou":
            curr_no_of_vowels += 1
        if inp_str[i - k] in "aeiou":
            curr_no_of_vowels -= 1

        global_no_of_vowels = max(global_no_of_vowels, curr_no_of_vowels)

    return global_no_of_vowels

print(max_no_of_vowels("abciiidef", 3) == 3)
print(max_no_of_vowels("aeiou", 2) == 2)
print(max_no_of_vowels("leetcode", 3) == 2)
print(max_no_of_vowels("rhythms", 4) == 0)
print(max_no_of_vowels("tryhard", 4) == 1)

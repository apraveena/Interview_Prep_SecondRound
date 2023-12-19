'''
You are given two strings - pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

Let's say that pattern matches a substring source[l..r] of source if the following three conditions are met:

they have equal length,
for each 0 in pattern the corresponding letter in the substring is a vowel,
for each 1 in pattern the corresponding letter is a consonant.
Your task is to calculate the number of substrings of source that match pattern.

Note: In this task we define the vowels as 'a', 'e', 'i', 'o', 'u', and 'y'. All other letters are consonants.

Example

For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
"010" matches source[0..2] = "ama", because both 0s match a, which is a vowel, and 1 match m, which is a consonant;
"010" doesn't match source[1..3] = "maz", because the first 0 corresponds to an m, which is a consonant, not a vowel;
"010" matches source[2..4] = "azi", because the first 0 matches an a (vowel), 1 matches z (consonant), and the second 0 matches i (vowel);
"010" doesn't match source[3..5] = "zin", because the first 0 corresponds to a consonant (z);
"010" doesn't match source[4..6] = "ing", because the second 0 corresponds to the letter g, which is a consonant.
So, there are only 2 matches.

For pattern = "100" and source = "codesignal", the output should be solution(pattern, source) = 0.

There are no double vowels in the string "codesignal", so it's not possible for any of its substrings to match this pattern.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string pattern

A string of 0s and 1s.

Guaranteed constraints:
1 ≤ pattern.length ≤ 103.

[input] string source

A string of lowercase English letters.

Guaranteed constraints:
1 ≤ source.length ≤ 103.

[output] integer

The number of substrings of source that match pattern.
'''
def solution(pattern, source):
    start = 0
    vowels = "aeiouy"
    slate = []
    count = 0
    if len(pattern) == len(source) == 1:
        return 1 if (pattern[0] == "0" and source[0] in vowels) \
        or (pattern[0] == "1" and source[0] not in vowels) else 0

    while start < len(source)-1:
        for i in range(0, len(pattern)):
            # if start == len(source)-2:
            #     break
            if (pattern[i] == "0" and source[start + i] in vowels) or (pattern[i] == "1" and source[start + i] not in vowels) :
                 slate.append(source[start + i])
            else:
                slate = []
                start += 1
                break

            if len(slate) == len(pattern):
                count += 1
                slate = []
                start += 1

    return count

print(solution("014", "amazing"))
print(solution("0", "y"))
print(solution("100", "codesignal"))
print(solution("010", "amazing"))

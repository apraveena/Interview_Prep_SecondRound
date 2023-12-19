'''
Comments from interviewer:
overall very good
learnings - I gave the optimal solution right away, luckily it worked..
            I thought it was Brute force solution, but turns out to be optimal O(n) solution
          - Others have also solved this problem using heapsort (need to look into that)

'''
'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

#auxiliary space - allowed - pros and cons
#may have numbers and special characters - ultimately all of it is a string
#string is of max size

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Interview Scaffolding
1. Fully understand the question by asking clarifying questions to the interviewer and considering edge cases.

2. Come up with brute force solution and optimal solution(s), if possible

3. Discuss the strengths and weaknesses of these approaches (time complexity, space complexity)

4. Choose the solution you think is optimal (or go with any solution if you can't come up with the optimal one) and write very high level sudo code

5. Ask the interviewer if you can start coding, code.

6. Come up with multiple test cases and walk through them (make sure to include edge cases from the first step!)

7. Talk about readability and refactor (if there is time!)
'''


def string_sort_decreasing(s):
    if not s or len(s) == 0:
        return s
    n = len(s)
    freq = {}
    # Calculate frequencies of each letter
    for ltr in s:
        freq[ltr] = freq.get(ltr, 0) + 1

    result = []
    # review this code again
    bucket = [[] for _ in range(n + 1)]

    # Iterate over hashmap to load the list with letters at the index of frequency
    for ltr, fq in freq.items():
        bucket[fq].append(ltr)

    # Iterate over the bucket to repeat adding the char with it's frequency
    for idx in range(len(bucket) - 1, 0, -1):
        inner_list = bucket[idx]
        if inner_list:
            for char in inner_list:
                for _ in range(idx):
                    result.append(char)

    return "".join(result)


print(string_sort_decreasing("c111111cc!24!acaa"))
































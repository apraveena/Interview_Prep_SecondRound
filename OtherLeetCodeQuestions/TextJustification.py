'''
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''
class Solution:
    from typing import List


    def fullJustify_my_try(self, words: List[str], maxWidth: int) -> List[str]:
        result, final, temp = [], [], []

        def format_result(self):
            for line in result:
                count = 0
                for elem in line:
                    count += len(elem)
                spaces = maxWidth - count
                gap = spaces//(len(line)-1)
                temp.append()


        curr_line = []
        len_so_far = 0
        for idx, word in enumerate(words):
            len_so_far = len_so_far + len(word) + 1 #1 for space
            curr_line.append(word)
            if len_so_far > maxWidth:
                curr_line.pop()
                result.append(curr_line[:])
                curr_line = [word]
                len_so_far = len(word) + 1

        result.append(curr_line[:])
        return format_result(result)

    #from https://www.youtube.com/watch?v=smaxL16J504
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        res = []

        i = 0  # pointer to keep track of where we are at
        curr_width = 0  # store the current width of the line

        curr_line = []

        while i < len(words):
            curr_word = words[i]
            if len(curr_word) + curr_width <= max_width:
                curr_line.append(curr_word)
                curr_width += len(curr_word) + 1
                i += 1
            else:
                # len(curr_line) to add the spaces back to total spaces
                spaces = max_width - curr_width + len(curr_line)

                added = 0
                j = 0

                while added < spaces:
                    if j >= len(curr_line) - 1:
                        j = 0
                    curr_line[j] += " "
                    added += 1
                    j += 1
                res.append("".join(curr_line))
                curr_line = []
                width = 0
            # last line
            for word in range(len(curr_line) - 1):
                curr_line[word] += " "
            curr_line[-1] += " " * (max_width - curr_width + 1)
            res.append("".join(curr_line))
            return res


sln = Solution()
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(sln.fullJustify(words, maxWidth))
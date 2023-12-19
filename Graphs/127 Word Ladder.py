'''
hard question
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
'''

from typing import List
from collections import deque

def ladderLength_mytry(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0
    # patterns = {}
    # for word in wordList:
    def get_pattern(word):
        temp = []
        for i in range(len(word)):
            temp.append(word[0:i] + "*" + word[i + 1: ])
        return temp[:]

    q = deque()
    q.append(beginWord)
    count = 1
    while q:
        curr_word = q.pop()
        pattern = get_pattern(curr_word)
        for word in wordList:
            if word != curr_word and set(pattern).intersection(get_pattern(word)):
                if endWord == word:
                    return count
                q.append(word)
        count += 1


    return count

from collections import defaultdict
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0
    patterns = {}
    wordList.append(beginWord)
    for word in wordList:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            if pattern in patterns:
                patterns[pattern].append(word)
            else:
                patterns[pattern] = [word]

    visited = {beginWord}
    q = deque([beginWord])
    count = 1
    while q:
        for i in range(len(q)):
            curr_word = q.popleft()
            if curr_word == endWord:
                return count
            for j in range(len(curr_word)):
                pattern = curr_word[:j] + "*" + curr_word[j + 1: ]
                for nei_word in patterns[pattern]:
                    if nei_word not in visited:
                        visited.add(nei_word)
                        q.append(nei_word)
        count += 1

    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# print(ladderLength(beginWord, endWord, wordList))


def string_transformation(words, start, stop):
        """
        Args:
         words(list_str)
         start(str)
         stop(str)
        Returns:
         list_str
        """
        if stop not in words:
            return -1

        patterns = {}
        for word in words:
            for i in range(len(start)):
                pattern = word[0:i] + "*" + word[i + 1:]
                if pattern in patterns:
                    patterns[pattern].append(word)
                else:
                    patterns[pattern] = [word]

        word_list = deque()
        count = 1
        word_list.append(start)
        path = [[] for _ in range(len(words))]
        visited = set()
        visited.add(start)

        while word_list:
            curr_word = word_list.popleft()
            if curr_word == stop:
                return count
            for j in range(len(start)):
                curr_pattern = curr_word[0:j] + "*" + curr_word[j + 1:]
                for pattern, nei_words in patterns.items():
                    for nei_word in nei_words:
                        if pattern == curr_pattern and nei_word not in visited:
                            if nei_word == stop:
                                return count
                            word_list.append(nei_word)
                            visited.add(nei_word)
            count += 1

        return -1



def string_transformation_return_path(words, start, stop):
    """
    Args:
     words(list_str)
     start(str)
     stop(str)
    Returns:
     list_str
    """
    patterns = {}
    if start not in words:
        words.append(start)
    for word in words:
        for i in range(len(start)):
            pattern = word[0:i] + "*" + word[i + 1:]
            if pattern in patterns:
                patterns[pattern].append(word)
            else:
                patterns[pattern] = [word]

    word_list = deque()
    temp = [start]
    word_list.append((start, temp))
    visited = set()
    visited.add(start)

    while word_list:
        curr_word, curr_path = word_list.popleft()

        # if curr_word == stop:
        #     temp.append(stop)
        #     return temp
        for j in range(len(start)):
            curr_pattern = curr_word[0:j] + "*" + curr_word[j + 1:]
            if curr_pattern not in patterns:
                continue
            for word in patterns[curr_pattern]:
                if word not in visited:
                    temp = curr_path[:]
                    temp.append(word)
                    if word == stop:
                        return temp
                    word_list.append((word, temp))
                    visited.add(word)

    temp.append(stop)
    return temp

print(string_transformation_return_path( ["cccw", "accc", "accw"], "cccc", "cccc") == ["cccc", "cccw", "cccc"])
print(string_transformation_return_path(["cat", "hat", "bad", "had"], "bat", "had") == ["bat", "hat", "had"])
print(string_transformation_return_path([], "bbb", "bbc") == ["bbb", "bbc"])
print(string_transformation_return_path(["cat", "cut", "cap", "map", "but","sit", "mat", "bat"], "cat", "bat") == ["cat", "bat"])
print(string_transformation_return_path(["cat", "cut", "cap", "map", "but","sit", "mat", "bat", "but"], "cat", "but") == ["cat", "bat", "but"])
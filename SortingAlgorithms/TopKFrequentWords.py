#nlogk
#Words must be sorted lexographically (alphabetical order)

from typing import List
import heapq

#following works
def k_most_frequent(k:int, words:List[str]) -> List[str]:
    """
    Args:
        k(int32): Number of words to be returned that occurred more
        words: List of words
    Returns:
        List[str] k number of words that occured most
    """
    hmap = {}
    for word in words:
        hmap[word] = hmap.get(word, 0) + 1

    #create a list of tuples. each tuple containing frequency and the word
    temp_list = [(-freq, word) for word, freq in hmap.items()] #negating frequency to use that build heap (more below)
    #Python heapa builds min heap by default.. by inversing the numbers we are reversing the order

    heapq.heapify(temp_list)
    # return [word for idx, (_, word) in enumerate(temp_list) if idx < 4] #using list comprehension
    return [heapq.heappop(temp_list)[1] for _ in range(k)]

#another way to use built-in function sorted
def k_most_frequent_again(k, words):
    """
    Args:
     k(int32)
     words(list_str)
    Returns:
     list_str
    """
    # hash_map = {}
    # for word in words:
    #     hash_map[word] = hash_map.get(word, 0) + 1
    #
    # res1 = sorted(hash_map.items(), key=lambda kv: (-kv[1], kv[0]))
    #
    # words = []
    # for i in range(k):
    #     words.append(res1[i][0])
    # return words

    hmap = {}
    for word in words:
        hmap[word] = hmap.get(word, 0) + 1

    temp_list = sorted(hmap.items(), key=lambda kv:(-kv[1], kv[0]))
    # words = []
    # for i in range(k):
    #     words.append(temp_list[i][0])
    # return words
    words = [temp_list[i][0] for i in range(k)]
    return words


#Doesn't work
def k_most_frequent_priority_queue_my_try(k, words):
    hmap = {}
    for word in words:
        hmap[word] = hmap.get(word, 0) + 1

    heap = []
    for word, freq in hmap.items():

        if len(heap) >= k:
            if freq > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, word))
            elif freq == heap[0][0] and word < heap[0][1]:  # if the same frequency item is found, then check the word
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, word))
        else:
            if len(heap)>0 and freq == heap[0][0] and word < heap[0][1]:
                popped = heapq.heappop(heap)
                heapq.heappush(heap, popped)

            heapq.heappush(heap, (freq, word))

    result = []
    while len(heap) > 0:
        result.append(heap.pop()[1])
    result.reverse()
    return result

#works - Yuval helped

class WordFreq:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        res = self.freq < other.freq or (self.freq == other.freq and self.word > other.word)
        return res

def k_most_frequent_priority_queue(k, words):
    hmap = {}
    for word in words:
        hmap[word] = hmap.get(word, 0) + 1

    print(hmap)
    heap = []
    for word, freq in hmap.items():
        cls1 = WordFreq(word, freq)
        if len(heap) >= k:
            if cls1 > heap[0] :
                heapq.heappop(heap)
                heapq.heappush(heap, cls1)
        else:
            heapq.heappush(heap, cls1)

    result = []
    while len(heap) > 0:
        result.append(heapq.heappop(heap).word)
    result.reverse()
    return result

lst = ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]
k = 4
print(k_most_frequent_again(k, lst))
#["car", "driver", "taxi", "bus"]

#heap is [(1, "bus"), (2, "driver"), (2, "taxi"), (3, "car")]
# lst = ["car", "bus", "driver", "bus", "taxi", "car", "driver", "candy", "race", "car", "car", "driver", "fare", "taxi", "bus", "bus"]
# k = 4
# lst = ["i","love","leetcode","i","love","coding"]
# k = 2
# print(k_most_frequent_priority_queue(k, lst))

# def test_k_most_frequent_priority_queue():
#     lst = ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]
#     k = 4
#     assert (k_most_frequent_priority_queue(k, lst)) == ["car", "driver", "taxi", "bus"]

from heapq import heapify, heappop


def k_most_frequent(k, words):
    """
    Args:
     k(int32)
     words(list_str)
    Returns:
     list_str
    """
    hmap = {}
    for word in words:
        hmap[word] = hmap.get(word, 0) + 1

    # negative frequency since heapify does a min heap and we need
    # max heap. By negating, we are reversing the order of elements
    temp_list = [(-freq, word) for word, freq in hmap.items()]
    heapify(temp_list)
    result = [heappop(temp_list)[1] for _ in range(k)]
    return result


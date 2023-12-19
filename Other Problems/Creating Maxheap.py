'''

Q 413 from Stack overflow
Python includes the heapq module for min-heaps, but I need a max heap.
What should I use for a max-heap implementation in Python?


The easiest way is to invert the value of the keys and use heapq.
For example, turn 1000.0 into -1000.0 and 5.0 into -5.0.

(or)

import heapq
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)

heapq.heappop(minheap)      # pop from minheap
heapq._heappop_max(maxheap) # pop from maxheap

(or)
The solution is to negate your values when you store them in the heap, or invert your object comparison like so:

import heapq

class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)
Example of a max-heap:

maxh = []
heapq.heappush(maxh, MaxHeapObj(x))
x = maxh[0].val  # fetch max value
x = heapq.heappop(maxh).val  # pop max value
But you have to remember to wrap and unwrap your values, which requires knowing if you are dealing with a min- or max-heap.

MinHeap, MaxHeap classes
Adding classes for MinHeap and MaxHeap objects can simplify your code:

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self, x): heapq.heappush(self.h, x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self, i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self, i): return self.h[i].val
Example usage:

minh = MinHeap()
maxh = MaxHeap()
# add some values
minh.heappush(12)
maxh.heappush(12)
minh.heappush(4)
maxh.heappush(4)
# fetch "top" values
print(minh[0], maxh[0])  # "4 12"
# fetch and remove "top" values
print(minh.heappop(), maxh.heappop())  # "4 12"

'''
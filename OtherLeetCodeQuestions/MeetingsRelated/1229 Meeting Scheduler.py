from typing import List

#time complexity - O(mlogm + nlogn) + O(m) + O(n) =
# runtime in leetcode = 602 ms
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if not slots1 or not slots2:
            return []

        if not slots1 and not slots2:
            return []

        slots1.sort()
        slots2.sort()
        slot1_ptr, slot2_ptr = 0, 0

        while slot1_ptr < len(slots1) and slot2_ptr < len(slots2):
            slot1 = slots1[slot1_ptr]
            slot2 = slots2[slot2_ptr]
            if slot1[0] == slot2[0] \
                    or slot2[0] < slot1[0] < slot2[1] \
                    or slot1[0] < slot2[0] < slot1[1]:
                overlap_start = max(slot1[0], slot2[0])
                overlap_end = min(slot1[1], slot2[1])
                overlap = overlap_end - overlap_start
                if duration <= overlap:
                    return [overlap_start, overlap_start + duration]
            if slot1[1] < slot2[1]:
                slot1_ptr += 1
            elif slot2[1] < slot1[1]:
                slot2_ptr += 1
            else:
                slot1_ptr += 1
                slot2_ptr += 1

        return []

#Another efficient with only 444 ms same time complexity as above
import heapq
class Solution1:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        heap1 = [(s,e) for s,e in slots1 if e-s >= duration]
        heap2 = [(s,e) for s,e in slots2 if e-s >= duration]
        heapq.heapify(heap1); heapq.heapify(heap2)
        while heap1 and heap2:
            (l1,r1), (l2,r2) = heap1[0], heap2[0]
            if l1 <= l2:
                if r1 <= l2:
                    heapq.heappop(heap1)
                elif r1 >= r2: # inner interval
                    if r2-l2 >= duration:
                        return [l2, l2+duration]
                    else:
                        heapq.heappop(heap2)
                else: # intersected
                    if r1-l2 >= duration:
                        return [l2, l2+duration]
                    else:
                        heapq.heappop(heap1)
            else:
                if r2 <= l1:
                    heapq.heappop(heap2)
                elif r2 >= r1: # inner interval
                    if r1-l1 >= duration:
                        return [l1, l1+duration]
                    else:
                        heapq.heappop(heap1)
                else: # intersected
                    if r2-l1 >= duration:
                        return [l1, l1+duration]
                    else:
                        heapq.heappop(heap2)
        return []

#Ran in 456 ms - added filter to eliminate slots that dont have enough duration and added variables
class Solution1:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if not slots1 or not slots2:
            return []

        slots1_updated = [[start, end] for start, end in slots1 if end - start >= duration]
        slots2_updated = [[start, end] for start, end in slots2 if end - start >= duration]

        slots1_updated.sort()
        slots2_updated.sort()
        slot1_ptr, slot2_ptr = 0, 0

        while slot1_ptr < len(slots1_updated) and slot2_ptr < len(slots2_updated):
            a_start, a_end = slots1_updated[slot1_ptr][0], slots1_updated[slot1_ptr][1]
            b_start, b_end = slots2_updated[slot2_ptr][0], slots2_updated[slot2_ptr][1]

            if a_start == b_start \
                    or b_start < a_start < b_end \
                    or a_start < b_start < a_end:
                overlap_start = max(a_start, b_start)
                overlap_end = min(a_end, b_end)
                overlap = overlap_end - overlap_start
                if duration <= overlap:
                    return [overlap_start, overlap_start + duration]
            # Increment pointer
            if a_end < b_end:
                slot1_ptr += 1
            elif b_end < a_end:
                slot2_ptr += 1
            else:
                slot1_ptr += 1
                slot2_ptr += 1

        return []

sln = Solution()
print(sln.minAvailableDuration([[0,2]], [[1,3]], 1) == [1, 2])
print(sln.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8) == [60,68])

from typing import List

#Not working - this is solution from leetcode solutions
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if not events:
            return 0
        events.sort(reverse=True)
        total_days = max(end for start, end in events)
        event_id = 0
        min_heap = []
        number_of_events_attended = 0

        for day in range(1, total_days + 1):
            # Add all the events that start today
            while event_id < len(events) and events[event_id][0] == day:
                heappush(min_heap, events[event_id][1])
                event_id += 1

            # remove all the events whose end date was before today
            while min_heap and min_heap[0] < day:
                heappop(min_heap)

            # if any event that cannot be attended today, attend it
            if min_heap:
                heappop(min_heap)
                number_of_events_attended += 1

        return number_of_events_attended


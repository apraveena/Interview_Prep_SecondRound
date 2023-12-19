from typing import List
import sys
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 0 or len(coordinates) == 1 or len(coordinates) == 2:
            return True
        coordinates.sort()

        for i in range(2, len(coordinates)):
            (x1, y1), (x2, y2) = coordinates[i - 2], coordinates[i - 1]
            (x3, y3) = coordinates[i]

            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False

        return True

def test_check_if_a_straight_line():
    sln = Solution()
    print(sln.checkStraightLine([[1,2],[2,3],[3,5]]) == False)
    print(sln.checkStraightLine([[0,0],[0,1],[0,-1]]) == True)
    print(sln.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) == False)
    print(sln.checkStraightLine([[[1,2],[2,3],[3,5]]]) == False)
from typing import List
def plusOne(digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
                if digits[i] == 9:
                        digits[i] = 0
                else:
                        digits[i] += 1
                        return digits
        new_digits = [0] * (len(digits) + 1)
        new_digits[0] = 1
        return new_digits



def plusOne1(digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
                if digits[i] < 9:
                        digits[i] += 1
                        return digits
                else:
                        digits[i] = 0
        #The following code is executed only if the list contains all 9s
        new_digits = [0] * (len(digits) + 1)
        new_digits[0] = 1
        return new_digits


print(plusOne([1, 2, 3]) == [1, 2, 4])
print(plusOne([4,3,2,1]) == [4, 3, 2, 2])
print(plusOne([9]) == [1, 0])
print(plusOne([9, 9]) == [1, 0, 0])
print(plusOne([3, 9, 9]) == [4, 0, 0])
print(plusOne([3, 9, 4]) == [3, 9, 5])
print(plusOne([9, 9, 9, 9]) == [1, 0, 0, 0, 0])
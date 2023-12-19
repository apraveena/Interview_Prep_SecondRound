from typing import List

def convert_num_to_list(n: int) -> List:
  str_num = str(n)
  res = []
  for i in range(len(str_num)):
    res.append(int(str_num[i]))
  return res

def isHappy(n: int) -> bool:
  lst = convert_num_to_list(n)
  used = []
  # if len(lst) == 1 :
  #   return lst[0] == 1
  while True:
    sum = 0
    for num in lst:
      sum += num ** 2

    if sum == 1:
      return True
    if sum < 3:
      return False
    if sum in used:
      return False
    used.append(sum)
    lst = convert_num_to_list(sum)

#Copied from javascript
def sumOfSquares(n: int) -> int:
  sum = 0
  while (n > 0):
    t = n % 10
    sum += (t * t)
    n/=10
  return sum

def isHappy1(n: int) -> bool:
  s = set()
  while (n != 1):
    temp = sumOfSquares(n)
    #?
    if temp in s:
      s.add(temp)
    else:
      return False
    n = temp
  return True


# print(isHappy(19) == True)
# print(isHappy(2) == False)
# print(isHappy(20) == False)
print(isHappy(7) == True)

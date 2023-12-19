'''Given a year, return the century it is in.
The first century spans from the year 1 up to and including the year 100,
the second - from the year 101 up to and including the year 200, etc.
'''


def solution(year):
    # 1-100 = first century
    # 101-200 = second century
    # 10
    # 1905 = 20 century

    if year <= 0:
        return -1

    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1


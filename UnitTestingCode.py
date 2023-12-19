import pytest

# from unittest import TestCase
#
# class TryTesting(TestCase):
#     def test_always_passes(self):
#         self.assertTrue(True)
#
#     def test_always_fails(self):
#         self.assertTrue(False)

def test_something():
    print("me".upper() == "ME")

def test_something_else():
    print("me".upper() == "MdE")

def add_1(num):
    return num + 1

def test_add_1():
    print(add_1(3) == 4)

def add_2(num):
    return num + 2

def test_add_2():
    assert add_2(3) == 5


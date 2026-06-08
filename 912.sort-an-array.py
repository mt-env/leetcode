# @leet imports start
from string import *
from re import *
from datetime import *
from collections import *
from heapq import *
from bisect import *
from copy import *
from math import *
from random import *
from statistics import *
from itertools import *
from functools import *
from operator import *
from io import *
from sys import *
from json import *
from builtins import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import statistics
import itertools
import functools
import operator
import io
import sys
import json
from typing import *
# @leet imports end

# @leet start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return Heap(nums).sorted()

class Heap:
    # root at 0
    # left child at 2n + 1, right child at 2n + 2
    # max heap so that when we lazily delete max, it ends up sorted
    def __init__(self, nums: list[int]):
        self.nums: list[int] = nums
        self.size: int = len(nums)
        for i in range(self.size // 2 - 1, -1, -1):
            self.percolate_down(i)
        print(f"printing heap: {self.nums}")

    def percolate_down(self, index: int) -> None:
        while True:
            if 2 * index + 1 >= self.size:
                return
            maxChild = -1
            if 2 * index + 2 >= self.size:
                maxChild = 2 * index + 1
            else:
                if self.nums[2 * index + 1] > self.nums[2 * index + 2]:
                    maxChild = 2 * index + 1
                else:
                    maxChild = 2 * index + 2
            if self.nums[index] < self.nums[maxChild]:
                self.swap(index, maxChild)
                index = maxChild
            else:
                return

    def swap(self, a: int, b: int) -> None:
        tmp = self.nums[a]
        self.nums[a] = self.nums[b]
        self.nums[b] = tmp

    def sorted(self) -> list[int]:
        while self.size != 0:
            self.swap(0, self.size - 1)
            self.size -= 1
            self.percolate_down(0)
        return self.nums

# @leet end

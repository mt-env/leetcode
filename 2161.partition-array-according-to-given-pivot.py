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
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return self.imperative(nums, pivot)

    def declarative(self, nums: List[int], pivot: int) -> List[int]:
        return ([x for x in nums if x < pivot] +
            [x for x in nums if x == pivot] +
            [x for x in nums if x > pivot])

    def imperative(self, nums: List[int], pivot: int) -> List[int]:
        less: list[int] = []
        equal: list[int] = []
        greater: list[int] = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        return less + equal + greater
# @leet end

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
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        out: list[int] = []
        left = 0
        right = 0

        while left < m and right < n:
            if nums1[left] < nums2[right]:
                out.append(nums1[left])
                left += 1
            else:
                out.append(nums2[right])
                right += 1

        while left < m:
            out.append(nums1[left])
            left += 1

        while right < n:
            out.append(nums2[right])
            right += 1

        nums1[:] = out
# @leet end

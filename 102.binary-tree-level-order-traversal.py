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
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
#         self.val: int = val
#         self.left: TreeNode | None = left
#         self.right: TreeNode | None = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q: deque[tuple[TreeNode | None, int]] = collections.deque()
        q.append((root, 0))

        result: list[list[int]] = []

        while len(q) != 0:
            curr = q.pop()
            if curr[0] is None:
                continue
            if curr[1] >= len(result):
                result.append([])
            result[curr[1]].append(curr[0].val)
            q.append((curr[0].right, curr[1] + 1))
            q.append((curr[0].left, curr[1] + 1))

        return result
# @leet end

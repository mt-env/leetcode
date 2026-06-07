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
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes: dict[int, TreeNode] = {}
        is_root: dict[int, bool] = {}
        for desc in descriptions:
            if not desc[0] in nodes:
                nodes[desc[0]] = TreeNode(desc[0])
                is_root[desc[0]] = True
            if not desc[1] in nodes:
                nodes[desc[1]] = TreeNode(desc[1])
                is_root[desc[1]] = True
            parent: TreeNode = nodes[desc[0]]
            child: TreeNode = nodes[desc[1]]
            is_root[desc[1]] = False
            if desc[2] == 1:
                parent.left = child
            else:
                parent.right = child
        for item in is_root:
            if is_root[item]:
                return nodes[item]

# @leet end

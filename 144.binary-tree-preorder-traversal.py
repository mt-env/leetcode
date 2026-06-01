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

class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: TreeNode | None = None,
            right: TreeNode | None = None
    ):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack: list[TreeNode | None] = []
        out: list[int] = []
        stack.append(root)
        while len(stack) != 0:
            curr = stack.pop()
            if curr == None:
                continue
            out.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
        return out

    def recursive_sol(self, root: Optional[TreeNode]) -> List[int]:
        list: list[int] = []
        self.traverse_rec(root, list)
        return list

    def traverse_rec(self, node: TreeNode | None, list: list[int]):
        if node == None:
            return
        list.append(node.val)
        self.traverse_rec(node.left, list)
        self.traverse_rec(node.right, list)

# @leet end

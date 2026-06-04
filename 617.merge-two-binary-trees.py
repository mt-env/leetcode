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
#     def __init__(
#             self,
#             val: int = 0,
#             left: TreeNode | None = None,
#             right: TreeNode | None = None
#     ):
#         self.val: int = val
#         self.left: TreeNode | None = left
#         self.right: TreeNode | None = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None and root2 == None:
            return None
        if root1 == None:
            return root2
        if root2 == None:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
# @leet end

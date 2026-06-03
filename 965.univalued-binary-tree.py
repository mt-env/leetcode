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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if root.left != None and root.val != root.left.val:
            return False
        if root.right != None and root.val != root.right.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
# @leet end

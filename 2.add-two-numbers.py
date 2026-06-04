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
# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val: int = 0, next: ListNode | None = None):
#         self.val: int = val
#         self.next: ListNode | None = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(l1, l2, False)

    def helper(self, l1: ListNode | None, l2: ListNode | None, carry: bool) -> ListNode | None:
        if l1 == None and l2 == None:
            return ListNode(1, None) if carry else None
        if l1 == None:
            return self.helper(ListNode(1, None), l2, False) if carry else l2
        if l2 == None:
            return self.helper(l1, ListNode(1, None), False) if carry else l1
        val = l1.val + l2.val + (1 if carry else 0)
        return ListNode(val % 10, self.helper(l1.next, l2.next, val >= 10))

# @leet end

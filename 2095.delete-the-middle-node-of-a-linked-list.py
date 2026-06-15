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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        node = head
        while node != None:
            len += 1
            node = node.next

        if len == 1:
            return None

        node = head
        for i in range(len):
            if node == None:
                continue
            if i == len // 2 - 1:
                node.next = node.next.next
            node = node.next
        return head

# @leet end

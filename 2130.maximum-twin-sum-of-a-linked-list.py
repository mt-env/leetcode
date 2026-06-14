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

class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val: int = val
        self.next: ListNode | None = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr: list[int] = []
        while head != None:
            arr.append(head.val)
            head = head.next

        max = arr[0] + arr[len(arr) - 1]
        for i in range(1, len(arr) // 2):
            if max < arr[i] + arr[len(arr) - i - 1]:
                max = arr[i] + arr[len(arr) - i - 1]
        return max

    def reversal(self, head: ListNode | None) -> int:
        reversed = None
        curr = head
        len = 0
        while curr != None:
            reversed = ListNode(curr.val, reversed)
            curr = curr.next
            len += 1

        forward_ptr = head
        reverse_ptr = reversed
        max = forward_ptr.val + reverse_ptr.val
        for i in range(len // 2):
            if forward_ptr.val + reverse_ptr.val > max:
                max = forward_ptr.val + reverse_ptr.val
            forward_ptr = forward_ptr.next
            reverse_ptr = reverse_ptr.next
        return max
# @leet end

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

    def bruteforce(self, A: list[int], B: list[int]) -> list[int]:
        C: list[int] = []
        for i in range(len(A)):
            A_sub = set(A[0:i+1])
            B_sub = set(B[0:i+1])
            C.append(len((A_sub.intersection(B_sub))))
        return C

    def freqarr(self, A: list[int], B: list[int]) -> list[int]:
        freq: list[int] = [0] * (len(A) + 1)
        C: list[int] = []
        curr_count = 0
        for i in range(len(A)):
            freq[A[i]] += 1
            if freq[A[i]] > 1:
                curr_count += 1
            freq[B[i]] += 1
            if freq[B[i]] > 1:
                curr_count += 1
            C.append(curr_count)
        return C

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        return self.freqarr(A, B)
# @leet end

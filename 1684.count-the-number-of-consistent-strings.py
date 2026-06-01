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
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_arr = [False] * 26
        for c in allowed:
            allowed_arr[ord(c) - ord('a')] = True
        consistent = len(words)
        for word in words:
            for c in word:
                if not allowed_arr[ord(c) - ord('a')]:
                    consistent -= 1
                    break
        return consistent

# @leet end

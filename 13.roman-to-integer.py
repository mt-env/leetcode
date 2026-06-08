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
    def romanToInt(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            print(f"count: {count}, i: {i}")
            if s[i] == 'I':
                if i + 1 < len(s) and s[i + 1] == 'V':
                    count += 4
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == 'X':
                    count += 9
                    i += 1
                else:
                    count += 1
            elif s[i] == 'V':
                count += 5
            elif s[i] == 'X':
                if i + 1 < len(s) and s[i + 1] == 'L':
                    count += 40
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == 'C':
                    count += 90
                    i += 1
                else:
                    count += 10
            elif s[i] == 'L':
                count += 50
            elif s[i] == 'C':
                if i + 1 < len(s) and s[i + 1] == 'D':
                    count += 400
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == 'M':
                    count += 900
                    i += 1
                else:
                    count += 100
            elif s[i] == 'D':
                count += 500
            elif s[i] == 'M':
                count += 1000
            i += 1
        return count

print(Solution().romanToInt("MCDLXXVI"))


# @leet end

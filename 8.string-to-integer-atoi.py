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
    def myAtoi(self, s: str) -> int:
        i: int = 0
        val: int = 0
        neg: bool = False
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] == '-':
            neg = True
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1
        while i < len(s) and s[i].isdigit():
            val *= 10
            val += int(s[i])
            i += 1
        val = -val if neg else val
        if val < -2**31:
            return -2**31
        if val > 2**31 - 1:
            return 2**31 - 1
        return val

# @leet end

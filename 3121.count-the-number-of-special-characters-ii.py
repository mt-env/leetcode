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
    def numberOfSpecialChars(self, word: str) -> int:
        count: list[int] = [0] * 26
        for c in word:
            idx = ord(c.lower()) - ord('a')
            if c.isupper():
                if count[idx] == 0:
                    count[idx] = 3
                if count[idx] == 1:
                    count[idx] = 2
            else:
                if count[idx] == 0:
                    count[idx] = 1
                elif count[idx] == 1:
                    continue
                elif count[idx] == 2:
                    count[idx] = 3
        result = 0
        for item in count:
            if item == 2:
                result += 1
        return result

# @leet end

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
        NEITHER, LOWER, UPPER, BOTH = range(4)
        status_list: dict[str, int] = {}
        for c in word:
            status = status_list.get(c.lower(), NEITHER)
            if c.islower():
                if status == NEITHER:
                    status_list[c.lower()] = LOWER
                if status == UPPER:
                    status_list[c.lower()] = BOTH
            if c.isupper():
                if status == NEITHER:
                    status_list[c.lower()] = UPPER
                if status == LOWER:
                    status_list[c.lower()] = BOTH

        count = 0
        for item in status_list:
            if status_list.get(item, NEITHER) == BOTH:
                count += 1
        return count



# @leet end

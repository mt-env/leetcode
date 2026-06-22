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
    def maxNumberOfBalloons(self, text: str) -> int:
        num_b = num_a = num_l = num_o = num_n = 0
        for c in text:
            if c == 'b':
                num_b += 1
            elif c == 'a':
                num_a += 1
            elif c == 'l':
                num_l += 1
            elif c == 'o':
                num_o += 1
            elif c == 'n':
                num_n += 1
        return min(num_b, num_a, num_l // 2, num_o // 2, num_n)

# @leet end

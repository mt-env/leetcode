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
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = nums[:n]
        second = nums[n:]
        out: list[int] = []
        for i in range(n):
            out.append(first[i])
            out.append(second[i])
        return out
# @leet end

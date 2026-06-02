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
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        groups: list[int] = []
        for i in range(0, len(s), k):
            groups.append(sum(map(int, s[i:i+k])))
        return self.digitSum(''.join(map(str, groups)), k)

# @leet end

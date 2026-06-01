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
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        total_cost = 0
        for i in range(len(cost)):
            if i % 3 == 2:
                continue
            total_cost += cost[i]
        return total_cost
# @leet end

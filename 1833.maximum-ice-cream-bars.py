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
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # counting sort
        mincost = min(costs)
        lencount = max(costs) - mincost + 1
        count = [0] * (lencount)
        for cost in costs:
            count[cost - mincost] += 1

        # count costs
        spent = 0
        bought = 0
        for i in range(lencount):
            cost = i + mincost
            end_cost = spent + count[i] * cost
            if end_cost > coins:
                return bought + ((coins - spent) // cost)
            spent = end_cost
            bought += count[i]
        return len(costs)


# @leet end

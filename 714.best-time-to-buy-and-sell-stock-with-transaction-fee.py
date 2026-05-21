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
    def maxProfit(self, prices: List[int], fee: int) -> int:
        arr: list[list[int]] = [[0] * 2] * (len(prices) + 1)
        for i in range(len(prices) - 1, -1, -1):
            arr[i][0] = max(
                -prices[i] - fee + arr[i + 1][1],
                arr[i + 1][0]
            )
            arr[i][1] = max(
                prices[i] + arr[i + 1][0],
                arr[i + 1][1]
            )
        return arr[0][0]

# @leet end

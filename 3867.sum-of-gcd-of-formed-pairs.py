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
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = [0] * len(nums)
        mx_i = nums[0]
        for i in range(len(nums)):
            mx_i = max(mx_i, nums[i])
            prefixGcd[i] = gcd(nums[i], mx_i)

        prefixGcd.sort()
        sum_gcd = 0
        for i in range(len(prefixGcd) // 2):
            sum_gcd += gcd(prefixGcd[i], prefixGcd[len(prefixGcd) - 1 - i])
        return sum_gcd

# @leet end

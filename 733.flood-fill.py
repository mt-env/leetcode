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
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack: list[tuple[int, int]] = list()
        stack.append((sr, sc))
        visited: set[tuple[int, int]] = set()
        while len(stack) != 0:
            (x, y) = stack.pop()
            if (x, y) in visited:
                continue
            curr = image[x][y]
            if x + 1 < len(image) and image[x + 1][y] == curr:
                stack.append((x + 1, y))
            if x - 1 >= 0 and image[x - 1][y] == curr:
                stack.append((x - 1, y))
            if y + 1 < len(image[x]) and image[x][y + 1] == curr:
                stack.append((x, y + 1))
            if y - 1 >= 0 and image[x][y - 1] == curr:
                stack.append((x, y - 1))
            image[x][y] = color
            visited.add((x, y))
        return image

# @leet end

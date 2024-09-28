from collections import defaultdict, deque, Counter
"""
SortedSetはhackされるのでハッシュ,
SortedListはhackされないので平衡二分探索木
"""
from sortedcontainers import SortedSet, SortedList, SortedDict
from heapq import heappush, heappop
from atcoder.dsu import DSU
from atcoder.segtree import SegTree
# st = SegTree(lambda dt1,dt2: データ参照, 単位元, 元データ)
from atcoder.lazysegtree import LazySegTree
# lst = LazySegTree(lambda dt1,dt2: データ参照, 単位元, lambda lz,dt: データ更新, lambda lz1,lz2: 遅延伝播, 恒等写像, 元データ)
from atcoder.modint import Modint, ModContext
from bisect import bisect_left, bisect_right
from itertools import product, groupby, permutations, combinations
import math
from copy import copy, deepcopy
import sys
sys.setrecursionlimit(10000000)
"""
！注意！
ABC328 E - Modulo MST 入出力例3にて,
実行時間が顕著に長くなった。
ex) 393ms -> 1570ms
必要なとき以外はコメントアウトしておく。
"""
"""
# PyPy再帰高速化
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
"""